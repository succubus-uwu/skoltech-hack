import spacy
import random
from pathlib import Path
from spacy.training import Example  # <-- НОВОЕ: Импортируем Example
from spacy.util import minibatch, compounding  # <-- НОВОЕ: Для батчинга

# Пример тренировочных данных (остаются без изменений в формате)
TRAIN_DATA = [
    ("Я живу в городе Москва на улице Ленина дом 51.", {
        "entities": [
            (9, 21, "CITY_FULL"),  # "городе Москва"
            (25, 37, "STREET_FULL"),  # "улице Ленина"
            (38, 41, "BUILDING_TYPE"),  # "дом"
            (42, 44, "BUILDING_NUMBER")  # "51"
        ]
    }),
    ("Мой офис расположен в городе Санкт-Петербург, Невский проспект 12.", {
        "entities": [
            (22, 42, "CITY_FULL"),  # "городе Санкт-Петербург"
            (44, 59, "STREET_FULL"),  # "Невский проспект"
            (60, 62, "BUILDING_NUMBER")  # "12"
        ]
    }),
    ("В деревне Гадюкино, улица Центральная, строение 3а.", {
        "entities": [
            (3, 19, "CITY_FULL"),  # "деревне Гадюкино"
            (21, 38, "STREET_FULL"),  # "улица Центральная"
            (40, 48, "BUILDING_TYPE"),  # "строение"
            (49, 51, "BUILDING_NUMBER")  # "3а"
        ]
    }),
    ("Нахожусь в Краснодаре, Пушкина 23, корпус 5.", {
        "entities": [
            (11, 20, "CITY_FULL"),  # "Краснодаре"
            (22, 29, "STREET_FULL"),  # "Пушкина"
            (30, 32, "BUILDING_NUMBER"),  # "23"
            (34, 40, "BUILDING_TYPE"),  # "корпус"
            (41, 42, "BUILDING_NUMBER")  # "5"
        ]
    }),
    ("Рядом с метро Выхино, проспект Рязанский 78.", {
        "entities": [
            (14, 20, "CITY_FULL"),  # "Выхино"
            (22, 39, "STREET_FULL"),  # "проспект Рязанский"
            (40, 42, "BUILDING_NUMBER")  # "78"
        ]
    })
]


def train_spacy_ner(train_data, n_iter=20, model_dir="./spacy_geo_model"):
    """
    Обучает SpaCy NER модель с кастомными метками.
    :param train_data: Список тренировочных данных в формате SpaCy (text, {"entities": ...}).
    :param n_iter: Количество эпох обучения.
    :param model_dir: Путь для сохранения обученной модели.
    """
    nlp = spacy.blank("ru")

    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe("ner", last=True)
    else:
        ner = nlp.get_pipe("ner")

    # Добавляем кастомные метки в NER
    for _, annotations in train_data:
        for ent in annotations.get("entities", []):  # Используем .get для безопасного доступа
            ner.add_label(ent[2])

    optimizer = nlp.begin_training()
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]

    with nlp.disable_pipes(other_pipes):  # only train NER
        for itn in range(n_iter):
            losses = {}
            # НОВОЕ: Преобразуем тренировочные данные в объекты Example
            # Каждый объект Example связывает "золотой стандарт" (размеченный Doc)
            # с текстом, который будет передан модели.
            # Для начала обучения с нуля, doc будет "чистым" текстом,
            # а аннотации будут в Example.

            examples = []
            for text, annotations in train_data:
                doc = nlp.make_doc(text)  # Создаем Doc из чистого текста
                # Example.from_dict принимает Doc объект и словарь с аннотациями
                examples.append(Example.from_dict(doc, annotations))

            random.shuffle(examples)  # Перемешиваем Example объекты для каждой эпохи

            # Создаем батчи из Example объектов
            # compounding используется для динамически меняющегося размера батча
            batches = minibatch(examples, size=compounding(4.0, 32.0, 1.001))

            for batch in batches:
                # НОВОЕ: nlp.update теперь принимает список объектов Example
                nlp.update(
                    batch,  # Пакет объектов Example
                    drop=0.5,  # вероятность дропаута
                    sgd=optimizer,  # оптимизатор
                    losses=losses
                )
            print(f"Epoch {itn + 1}, Losses: {losses}")

    output_dir = Path(model_dir)
    if not output_dir.exists():
        output_dir.mkdir(parents=True)
    nlp.to_disk(output_dir)
    print(f"Модель сохранена в {output_dir}")

    return nlp


# Запускаем обучение
trained_nlp = train_spacy_ner(TRAIN_DATA, n_iter=30)

# Далее ваш код для тестирования модели
# Загрузка обученной модели
output_dir = "./spacy_geo_model"
nlp_loaded = spacy.load(output_dir)

# Тестовое предложение
test_text = "Я работаю в Москве, на проспекте Мира, дом 10, корпус 2."

# Обработка текста моделью
doc = nlp_loaded(test_text)

print(f"\nТестирование модели на тексте: '{test_text}'")
print("-" * 50)

# Вывод сущностей, как их распознала модель
for ent in doc.ents:
    print(f"Сущность: '{ent.text}' | Тип: '{ent.label_}' | Диапазон: [{ent.start_char}, {ent.end_char}]")

print("-" * 50)

# Пост-обработка для вашего желаемого формата
processed_output = []
last_end_char = 0

for ent in doc.ents:
    if ent.start_char > last_end_char:
        non_entity_text = test_text[last_end_char: ent.start_char].strip()
        if non_entity_text:
            processed_output.append(f"{non_entity_text}(пропуск)")

    semantic_type = ""
    if ent.label_ == "CITY_FULL":
        if "город" in ent.text.lower():
            semantic_type = "город"
        elif "деревн" in ent.text.lower():
            semantic_type = "деревня"
        elif "сел" in ent.text.lower():
            semantic_type = "село"
        else:
            semantic_type = "населенный пункт"
    elif ent.label_ == "STREET_FULL":
        if "улица" in ent.text.lower():
            semantic_type = "улица"
        elif "проспект" in ent.text.lower():
            semantic_type = "проспект"
        elif "переулок" in ent.text.lower():
            semantic_type = "переулок"
        else:
            semantic_type = "улица"
    elif ent.label_ == "BUILDING_TYPE":
        semantic_type = "тип строения"
    elif ent.label_ == "BUILDING_NUMBER":
        semantic_type = "номер строения"

    processed_output.append(f'"{ent.text}" ({semantic_type})')
    last_end_char = ent.end_char

if last_end_char < len(test_text):
    non_entity_text = test_text[last_end_char:].strip()
    if non_entity_text:
        processed_output.append(f"{non_entity_text}(пропуск)")

print("\nВаш желаемый формат вывода:")
print(" ".join(processed_output))
