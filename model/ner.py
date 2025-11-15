import random
from pathlib import Path

import spacy

from model.data.train_ner import TRAIN_DATA


def train_spacy_ner(train_data, n_iter=20, model_dir="./spacy_geo_model"):
    """
    Обучает SpaCy NER модель с кастомными метками.
    :param train_data: Список тренировочных данных в формате SpaCy.
    :param n_iter: Количество эпох обучения.
    :param model_dir: Путь для сохранения обученной модели.
    """
    # 1. Создаем пустую русскую модель
    # Если бы мы хотели дообучить существующую модель, использовали бы spacy.load("ru_core_web_sm")
    nlp = spacy.blank("ru")

    # 2. Добавляем компонент NER в конвейер обработки
    # 'ner' pipe должен быть в конце конвейера
    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe("ner", last=True)
    else:
        ner = nlp.get_pipe("ner")

    # 3. Добавляем кастомные метки в NER
    for _, annotations in train_data:
        for ent in annotations.get("entities"):
            ner.add_label(ent[2]) # ent[2] это 'МЕТКА'

    # 4. Инициализация оптимизатора и тренировочного цикла
    # Отключаем другие компоненты конвейера на время обучения NER, если они есть
    # (в spacy.blank их нет, но это хорошая практика)
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
    with nlp.disable_pipes(other_pipes):  # only train NER
        optimizer = nlp.begin_training()
        for itn in range(n_iter):
            random.shuffle(train_data)
            losses = {}
            for text, annotations in train_data:
                # Обновляем модель
                nlp.update(
                    [text],         # пакет текста
                    [annotations],  # пакет аннотаций
                    drop=0.5,       # вероятность дропаута, помогает избежать переобучения
                    sgd=optimizer,  # оптимизатор
                    losses=losses
                )
            print(f"Epoch {itn + 1}, Losses: {losses}")

    # 5. Сохранение обученной модели
    output_dir = Path(model_dir)
    if not output_dir.exists():
        output_dir.mkdir(parents=True)
    nlp.to_disk(output_dir)
    print(f"Модель сохранена в {output_dir}")

    return nlp

# Запускаем обучение
trained_nlp = train_spacy_ner(TRAIN_DATA, n_iter=30)

# Загрузка обученной модели
# Если вы запустили тренировку и она сохранила модель, то просто загружаем её
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
# Я живу в(пропуск) "город Москва" (город) на(пропуск) "улице Ленина" (улица) дом (тип строения) 51(номер строения)
processed_output = []
last_end_char = 0

for ent in doc.ents:
    # Добавляем пропуски (текст между сущностями)
    if ent.start_char > last_end_char:
        non_entity_text = test_text[last_end_char: ent.start_char].strip()
        if non_entity_text:
            processed_output.append(f"{non_entity_text}(пропуск)")

    # Определяем семантический тип для вывода
    semantic_type = ""
    if ent.label_ == "CITY_FULL":
        # Проверяем наличие слов-маркеров типа "город", "деревня", "село"
        if "город" in ent.text.lower():
            semantic_type = "город"
        elif "деревн" in ent.text.lower():  # "деревне", "деревня"
            semantic_type = "деревня"
        elif "сел" in ent.text.lower():  # "село", "селе"
            semantic_type = "село"
        else:
            semantic_type = "населенный пункт"  # По умолчанию
    elif ent.label_ == "STREET_FULL":
        if "улица" in ent.text.lower():
            semantic_type = "улица"
        elif "проспект" in ent.text.lower():
            semantic_type = "проспект"
        elif "переулок" in ent.text.lower():
            semantic_type = "переулок"
        else:
            semantic_type = "улица"  # По умолчанию
    elif ent.label_ == "BUILDING_TYPE":
        semantic_type = "тип строения"
    elif ent.label_ == "BUILDING_NUMBER":
        semantic_type = "номер строения"

    processed_output.append(f'"{ent.text}" ({semantic_type})')
    last_end_char = ent.end_char

# Добавляем оставшийся текст после последней сущности
if last_end_char < len(test_text):
    non_entity_text = test_text[last_end_char:].strip()
    if non_entity_text:
        processed_output.append(f"{non_entity_text}(пропуск)")

print("\nВаш желаемый формат вывода:")
print(" ".join(processed_output))
