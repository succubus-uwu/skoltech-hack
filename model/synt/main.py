secret = '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'
import datetime

import asyncio

import anthropic
import httpx
import spacy

from address import AddressGenerator, AddressClassifier
from normalizer import Normalizer

nlp = spacy.blank("ru")

train_data = []


async def main_with_progress():
    client = anthropic.AsyncAnthropic(
        api_key=secret,
        base_url="http://95.164.119.230:9090/anthropic",
        http_client=httpx.AsyncClient(verify=False)
    )
    n = Normalizer()

    all_addresses = []
    total_batches = 2
    completed_batches = 0

    generator = AddressGenerator(client, normalizer=n, count=50)
    classifier = AddressClassifier(client, n)

    print("Начинаем параллельную генерацию 100 адресов...")

    # Генерация батчей

    for batch_num in range(0, total_batches, 2):  # По 3 батча за раз
        current_batch_count = min(2, total_batches - batch_num)

        print(f"Генерация батчей {batch_num + 1}-{batch_num + current_batch_count}...")

        batch_addresses = await generator.generate_addresses_batch(
            batch_count=current_batch_count,
            concurrency_limit=current_batch_count
        )

        all_addresses.extend(batch_addresses)
        completed_batches += current_batch_count
        print(f"Завершено: {completed_batches}/{total_batches} батчей, собрано {len(all_addresses)} адресов")

    print(f"Итоговое количество сгенерированных адресов: {len(all_addresses)}")

    # Классификация с прогрессом
    print("Начинаем классификацию...")
    batch_size = 50  # Классифицируем по 20 адресов за раз

    for i in range(0, len(all_addresses), batch_size):
        batch = all_addresses[i:i + batch_size]
        print(f"Классификация батча {i // batch_size + 1}/{(len(all_addresses) + batch_size - 1) // batch_size}...")

        batch_results = await classifier.classify_addresses_batch(batch)

        for address, (normalized_text, classification) in zip(batch, batch_results):
            train_data.append((normalized_text, classification))

    print(f"Обработано всего: {len(train_data)} адресов")


def save_pretty(data, filename):
    """Читабельное сохранение"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f'"""\n')
        f.write(f'Training Data for Address NER\n')
        f.write(f'Generated: {datetime.datetime.now()}\n')
        f.write(f'Total samples: {len(data)}\n')
        f.write(f'"""\n\n')
        f.write("train_data = [\n")

        for i, (text, classification) in enumerate(data, 1):
            f.write(f"    # Sample {i}\n")
            f.write(f"    (\n")
            f.write(f"        {repr(text)},\n")
            f.write(f"        {classification}\n")
            f.write(f"    ),\n\n")

        f.write("]\n")
    print(f"✓ Сохранено в {filename}")

if __name__ == "__main__":
    asyncio.run(main_with_progress())
    print(f"\nИтоговое количество данных для обучения: {len(train_data)}")
    print("\nПримеры данных:")
    #
    # from train_pretty1 import train_data as data1
    # from train_pretty2 import train_data as data2
    # from train_pretty3 import train_data as data3
    # from train_pretty4 import train_data as data4
    # from train_pretty5 import train_data as data5
    # from train_pretty6 import train_data as data6
    # from train_pretty7 import train_data as data7
    # from train_pretty8 import train_data as data8
    # from train_pretty9 import train_data as data9
    # from train_pretty10 import train_data as data10
    #
    # train_data = (
    #         data1 + data2 + data3 + data4 + data5 +
    #         data6 + data7 + data8 + data9 + data10
    # )

    print(f"Общее количество примеров: {len(train_data)}")

    save_pretty(train_data, "train_pretty9.py")

import collections
import re
from typing import List, Tuple, Dict


def analyze_training_data(train_data: List[Tuple[str, Dict]]) -> Dict:
    """
    Анализирует тренировочные данные и возвращает статистику
    """

    # 1. Частота комбинаций меток (порядок важен)
    combination_freq_ordered = collections.Counter()

    # 1.1. Частота комбинаций меток (порядок НЕ важен - перестановки)
    combination_freq_unordered = collections.Counter()

    # 2. Частота каждой метки
    label_freq = collections.Counter()

    # 3. Статистика по токенам
    total_entities = 0
    total_tokens_in_entities = 0
    entity_token_counts = []

    # 4. Статистика по токенам для каждого типа сущности
    label_token_stats = collections.defaultdict(list)

    # 5. Статистика по типам улиц и корпусов
    street_type_stats = collections.Counter()
    corpus_stats = collections.Counter()

    for text, annotations in train_data:
        entities = annotations['entities']

        # Сортируем сущности по позиции в тексте
        sorted_entities = sorted(entities, key=lambda x: x[0])
        labels_in_order = [label for start, end, label in sorted_entities]

        # 1. Частота комбинаций (порядок важен)
        if labels_in_order:
            combination_key_ordered = ' -> '.join(labels_in_order)
            combination_freq_ordered[combination_key_ordered] += 1

            # 1.1. Частота комбинаций (порядок НЕ важен)
            combination_key_unordered = ' + '.join(sorted(labels_in_order))
            combination_freq_unordered[combination_key_unordered] += 1

        # 2. Частота каждой метки и статистика по токенам
        for start, end, label in entities:
            label_freq[label] += 1
            total_entities += 1

            entity_text = text[start:end]
            tokens_in_entity = len(entity_text.split())

            total_tokens_in_entities += tokens_in_entity
            entity_token_counts.append(tokens_in_entity)
            label_token_stats[label].append(tokens_in_entity)

        # 5. Анализ паттернов в тексте
        # Типы улиц
        street_patterns = {
            'улица': r'\bулица\b|\bул\b|\bул\.',
            'проспект': r'\bпроспект\b|\bпр\b|\bпр\.|\bпр-т\b',
            'переулок': r'\bпереулок\b|\bпер\b|\bпер\.',
            'бульвар': r'\bбульвар\b|\bбул\b|\bбул\.',
            'шоссе': r'\bшоссе\b|\bш\b|\bш\.',
            'проезд': r'\bпроезд\b|\bпр-д\b',
            'аллея': r'\bаллея\b|\bал\b',
            'набережная': r'\bнабережная\b|\bнаб\b|\bнаб\.',
            'площадь': r'\bплощадь\b|\bпл\b|\bпл\.'
        }

        for street_type, pattern in street_patterns.items():
            if re.search(pattern, text, re.IGNORECASE):
                street_type_stats[street_type] += 1

        # Корпусы
        corpus_patterns = {
            'корпус': r'\bкорпус\b|\bкорп\b|\bкорп\.',
            'к_одиночная': r'\bк\b|\bк\.',
            'к_с_номером': r'\bк\d+\b',
            'строение': r'\bстроение\b|\bстр\b|\bстр\.',
            'строение_с_номером': r'\bстр\d+\b',
            'дом': r'\bдом\b|\bд\b|\bд\.',
            'дом_с_номером': r'\bд\d+\b'
        }

        for corpus_type, pattern in corpus_patterns.items():
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                corpus_stats[corpus_type] += len(matches)

    # Расчет средних значений
    avg_tokens_per_entity = total_tokens_in_entities / total_entities if total_entities > 0 else 0

    # Статистика по токенам для каждого типа сущности
    label_token_summary = {}
    for label, token_counts in label_token_stats.items():
        label_token_summary[label] = {
            'count': len(token_counts),
            'avg_tokens': sum(token_counts) / len(token_counts),
            'min_tokens': min(token_counts),
            'max_tokens': max(token_counts),
            'total_tokens': sum(token_counts)
        }

    return {
        'combination_frequency_ordered': dict(combination_freq_ordered.most_common()),
        'combination_frequency_unordered': dict(combination_freq_unordered.most_common()),
        'label_frequency': dict(label_freq.most_common()),
        'token_statistics': {
            'total_entities': total_entities,
            'total_tokens_in_entities': total_tokens_in_entities,
            'avg_tokens_per_entity': avg_tokens_per_entity,
            'min_tokens_per_entity': min(entity_token_counts) if entity_token_counts else 0,
            'max_tokens_per_entity': max(entity_token_counts) if entity_token_counts else 0
        },
        'label_token_statistics': label_token_summary,
        'street_type_statistics': dict(street_type_stats.most_common()),
        'corpus_statistics': dict(corpus_stats.most_common())
    }


# Анализ ваших данных
stats = analyze_training_data(train_data)

# Вывод результатов
print("=== СТАТИСТИКА ТРЕНИРОВОЧНЫХ ДАННЫХ ===\n")

print("1. ЧАСТОТА КОМБИНАЦИЙ МЕТОК (порядок ВАЖЕН):")
for combination, count in stats['combination_frequency_ordered'].items():
    print(f"   {combination}: {count} раз")

print("\n1.1. ЧАСТОТА КОМБИНАЦИЙ МЕТОК (порядок НЕ важен, перестановки):")
for combination, count in stats['combination_frequency_unordered'].items():
    print(f"   {combination}: {count} раз")

print("\n2. ЧАСТОТА КАЖДОЙ МЕТКИ:")
for label, count in stats['label_frequency'].items():
    percentage = (count / stats['token_statistics']['total_entities']) * 100
    print(f"   {label}: {count} раз ({percentage:.1f}%)")

print("\n3. ОБЩАЯ СТАТИСТИКА ПО ТОКЕНАМ:")
token_stats = stats['token_statistics']
print(f"   Всего сущностей: {token_stats['total_entities']}")
print(f"   Всего токенов в сущностях: {token_stats['total_tokens_in_entities']}")
print(f"   Среднее токенов на сущность: {token_stats['avg_tokens_per_entity']:.2f}")
print(f"   Минимальное токенов в сущности: {token_stats['min_tokens_per_entity']}")
print(f"   Максимальное токенов в сущности: {token_stats['max_tokens_per_entity']}")

print("\n4. СТАТИСТИКА ПО ТОКЕНАМ ДЛЯ КАЖДОГО ТИПА СУЩНОСТИ:")
for label, label_stats in stats['label_token_statistics'].items():
    print(f"   {label}:")
    print(f"     Количество: {label_stats['count']}")
    print(f"     Среднее токенов: {label_stats['avg_tokens']:.2f}")
    print(f"     Минимальное токенов: {label_stats['min_tokens']}")
    print(f"     Максимальное токенов: {label_stats['max_tokens']}")
    print(f"     Всего токенов: {label_stats['total_tokens']}")

print("\n5. СТАТИСТИКА ПО ТИПАМ УЛИЦ:")
for street_type, count in stats['street_type_statistics'].items():
    print(f"   {street_type}: {count} раз")

print("\n6. СТАТИСТИКА ПО КОРПУСАМ:")
for corpus_type, count in stats['corpus_statistics'].items():
    print(f"   {corpus_type}: {count} раз")

# Дополнительная сводка по корпусам
total_corpus_mentions = sum(stats['corpus_statistics'].values())
print(f"\n   Всего упоминаний корпусов: {total_corpus_mentions}")