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


def train_spacy_ner(train_data, n_iter=3000, model_dir="./spacy_geo_model"):
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

        if itn % 500 == 0:
            print(f"Epoch {itn}, Loss: {losses['ner']:.4f}")

    # Тест ДО сохранения
    text, _ = train_data[0]
    doc = nlp(text)
    print(f"\n✓ Результат ДО сохранения: {[(ent.text, ent.label_) for ent in doc.ents]}")

    # === СОХРАНЕНИЕ МОДЕЛИ ===
    output_dir = Path(model_dir)
    if output_dir.exists():
        import shutil
        shutil.rmtree(output_dir)  # Удаляем старую модель!

    output_dir.mkdir(parents=True, exist_ok=True)
    nlp.to_disk(output_dir)
    print(f"\n✓ Модель сохранена в {output_dir}")

    return nlp


# Обучение
trained_nlp = train_spacy_ner(TRAIN_DATA, n_iter=3000)

# === ТЕСТ ПОСЛЕ ЗАГРУЗКИ ===
print("\n" + "=" * 70)
print("ТЕСТ: Загрузка модели с диска")
print("=" * 70)

output_dir = "./spacy_geo_model"
nlp_loaded = spacy.load(output_dir)

test_text = "Я живу в городе Москва на улице Ленина дом 51."
doc = nlp_loaded(test_text)

print(f"\nТекст: '{test_text}'")
print(f"✓ Результат ПОСЛЕ загрузки:")
for ent in doc.ents:
    print(f"  '{ent.text}' -> {ent.label_}")
