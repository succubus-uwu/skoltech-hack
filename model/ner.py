import spacy
import random
from pathlib import Path
from spacy.training import Example
from model.data.train_data import TRAIN_DATA
from spacy.util import minibatch, compounding
from spacy.training import offsets_to_biluo_tags

"Я жить город Москва улица Ленин дом 51"

# Пример тренировочных данных (остаются без изменений в формате)




def train_spacy_ner(train_data, n_iter=30, model_dir="./spacy_geo_model"):
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
trained_nlp = train_spacy_ner(TRAIN_DATA, n_iter=30)

# === ТЕСТ ПОСЛЕ ЗАГРУЗКИ ===
print("\n" + "=" * 70)
print("ТЕСТ: Загрузка модели с диска")
print("=" * 70)

output_dir = "./spacy_geo_model"
nlp_loaded = spacy.load(output_dir)

while True:
    test_text = input("москва ул арбат далее 28 кв 15: ")
    doc = nlp_loaded(test_text)

    print(f"\nТекст: '{test_text}'")
    print(f"✓ Результат ПОСЛЕ загрузки:")
    for ent in doc.ents:
        print(f"  '{ent.text}' -> {ent.label_}")
