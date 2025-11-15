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


def train_spacy_ner(train_data, n_iter=30000, model_dir="./spacy_geo_model"):
    """
    Обучаем NER с нуля, без базовой модели
    """
    # Создаем пустую русскую модель
    nlp = spacy.blank("ru")

    # Добавляем ТОЛЬКО NER компонент
    ner = nlp.add_pipe("ner")

    # Добавляем наши метки
    for _, annotations in train_data:
        for ent in annotations.get("entities", []):
            ner.add_label(ent[2])

    print(f"Метки NER: {ner.labels}")

    # Создаем примеры
    examples = []
    for text, annotations in train_data:
        doc = nlp.make_doc(text)
        examples.append(Example.from_dict(doc, annotations))

    # Инициализируем
    nlp.initialize(lambda: examples)

    # Обучаем
    for itn in range(n_iter):
        losses = {}
        random.shuffle(examples)
        nlp.update(examples, drop=0.5, losses=losses)

        if itn % 10 == 0:
            print(f"Epoch {itn}, Loss: {losses['ner']:.4f}")

    # Тест
    text, _ = train_data[0]
    doc = nlp(text)
    print(f"\nРезультат: {[(ent.text, ent.label_) for ent in doc.ents]}")

    return nlp


# Запускаем обучение
trained_nlp = train_spacy_ner(TRAIN_DATA, n_iter=3000)

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
