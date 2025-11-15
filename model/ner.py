import spacy
import random
from pathlib import Path
from spacy.training import Example
from spacy.util import minibatch, compounding
from spacy.training import offsets_to_biluo_tags

"Я жить город Москва улица Ленин дом 51"

# Пример тренировочных данных (остаются без изменений в формате)
TRAIN_DATA = [
    ("Я живу в городе Москва на улице Ленина дом 51.", {
        "entities": [
            (9, 22, "CITY_FULL"),  # "городе Москва"
            (26, 38, "STREET_FULL"),  # "улице Ленина"
            (39, 42, "BUILDING_TYPE"),  # "дом"
            (43, 45, "BUILDING_NUMBER")  # "51"
        ]
    }),
    # ("Мой офис расположен в городе Санкт-Петербург, Невский проспект 12.", {
    #     "entities": [
    #         (22, 42, "CITY_FULL"),  # "городе Санкт-Петербург"
    #         (44, 59, "STREET_FULL"),  # "Невский проспект"
    #         (60, 62, "BUILDING_NUMBER")  # "12"
    #     ]
    # }),
    # ("В деревне Гадюкино, улица Центральная, строение 3а.", {
    #     "entities": [
    #         (3, 19, "CITY_FULL"),  # "деревне Гадюкино"
    #         (21, 38, "STREET_FULL"),  # "улица Центральная"
    #         (40, 48, "BUILDING_TYPE"),  # "строение"
    #         (49, 51, "BUILDING_NUMBER")  # "3а"
    #     ]
    # }),
    # ("Нахожусь в Краснодаре, Пушкина 23, корпус 5.", {
    #     "entities": [
    #         (11, 20, "CITY_FULL"),  # "Краснодаре"
    #         (22, 29, "STREET_FULL"),  # "Пушкина"
    #         (30, 32, "BUILDING_NUMBER"),  # "23"
    #         (34, 40, "BUILDING_TYPE"),  # "корпус"
    #         (41, 42, "BUILDING_NUMBER")  # "5"
    #     ]
    # }),
    # ("Рядом с метро Выхино, проспект Рязанский 78.", {
    #     "entities": [
    #         (14, 20, "CITY_FULL"),  # "Выхино"
    #         (22, 39, "STREET_FULL"),  # "проспект Рязанский"
    #         (40, 42, "BUILDING_NUMBER")  # "78"
    #     ]
    # })
]


def train_spacy_ner(train_data, n_iter=30, model_dir="./spacy_geo_model"):
    """
    Обучает SpaCy NER модель с кастомными метками, используя ru_core_news_sm как базу.
    :param train_data: Список тренировочных данных в формате SpaCy (text, {"entities": ...}).
    :param n_iter: Количество эпох обучения.
    :param model_dir: Путь для сохранения обученной модели.
    """
    # 1. Загружаем уже существующую русскую модель ru_core_news_sm
    nlp = spacy.load("ru_core_news_sm")
    print(f"Используем базовую модель: {nlp.meta['name']}")

    # 2. Получаем компонент NER
    # ru_core_news_sm уже имеет компонент 'ner'
    if "ner" not in nlp.pipe_names:
        # Это маловероятно для ru_core_news_sm, но хорошая проверка
        ner = nlp.add_pipe("ner", last=True)
    else:
        ner = nlp.get_pipe("ner")

    # 3. Добавляем кастомные метки в NER
    for _, annotations in train_data:
        for ent in annotations.get("entities", []):
            if ent[2] not in ner.labels:  # Проверяем, чтобы не добавлять метку, если она уже есть
                ner.add_label(ent[2])

    # Отображаем все метки, которые теперь знает NER компонент
    print(f"Все метки NER: {ner.labels}")

    # --- ДОБАВЬТЕ ЭТОТ ОТЛАДОЧНЫЙ КОД ---
    print("\n--- Проверка выравнивания сущностей ---")
    for text, annotations in TRAIN_DATA:
        doc = nlp.make_doc(text)
        entities = annotations.get("entities", [])
        biluo_tags = offsets_to_biluo_tags(doc, entities)

        # Если есть пропущенные (misaligned) сущности
        if '-' in biluo_tags:
            print(f"\nПроблема с текстом: '{text}'")
            print(f"Аннотации: {entities}")
            print("Токены и их BILUO-теги:")
            for token, tag in zip(doc, biluo_tags):
                print(f"  '{token.text}' -> {tag}")
            print("---")
    # --- КОНЕЦ ОТЛАДОЧНОГО КОДА ---

    optimizer = nlp.begin_training()
    # Отключаем другие компоненты конвейера на время обучения NER
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
    with nlp.disable_pipes(other_pipes):
        for itn in range(n_iter):
            losses = {}
            examples = []
            for text, annotations in train_data:
                # В случае дообучения, Doc объект должен быть создан с помощью nlp
                # чтобы он содержал всю предварительную информацию (токены, части речи и т.д.)
                doc = nlp.make_doc(text)
                examples.append(Example.from_dict(doc, annotations))

            random.shuffle(examples)

            batches = minibatch(examples, size=compounding(4.0, 32.0, 1.001))

            for batch in batches:
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
test_text = "Я живу в городе Москва на улице Ленина дом 51."

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
