import spacy
import random
import json
from pathlib import Path
from spacy.training import Example
from spacy.scorer import Scorer
from sklearn.model_selection import train_test_split
from collections import defaultdict
from datetime import datetime
from typing import List, Tuple, Dict
import warnings

warnings.filterwarnings('ignore')

from model.data.train_data_fixed_housenumber import TRAIN_DATA


class NERTrainer:
    """
    Профессиональный тренер для SpaCy NER моделей (консольная версия)
    """

    def __init__(self, train_data: List[Tuple], model_dir: str = "./spacy_geo_model"):
        self.train_data = train_data
        self.model_dir = Path(model_dir)
        self.nlp = None
        self.history = {
            'epoch': [],
            'train_loss': [],
            'val_precision': [],
            'val_recall': [],
            'val_f1': []
        }
        self.best_f1 = 0.0
        self.best_model_path = None

    def validate_annotations(self):
        """
        Проверяет корректность разметки перед обучением
        """
        print("=" * 70)
        print("ВАЛИДАЦИЯ РАЗМЕТКИ")
        print("=" * 70)

        # Создаем временную модель для проверки
        nlp_temp = spacy.blank("ru")

        issues = []
        for idx, (text, annotations) in enumerate(self.train_data):
            doc = nlp_temp.make_doc(text)
            entities = annotations.get("entities", [])

            # Проверяем выравнивание
            from spacy.training import offsets_to_biluo_tags
            try:
                biluo_tags = offsets_to_biluo_tags(doc, entities)
                if '-' in biluo_tags:
                    issues.append({
                        'index': idx,
                        'text': text,
                        'problem': 'Misaligned entities',
                        'entities': entities
                    })
            except Exception as e:
                issues.append({
                    'index': idx,
                    'text': text,
                    'problem': str(e),
                    'entities': entities
                })

        if issues:
            print(f"⚠️  Найдено {len(issues)} проблем в разметке:\n")
            for issue in issues[:5]:  # Показываем первые 5
                print(f"Пример #{issue['index']}: {issue['text'][:50]}...")
                print(f"  Проблема: {issue['problem']}")
                print(f"  Entities: {issue['entities']}\n")

            if len(issues) > 5:
                print(f"... и еще {len(issues) - 5} проблем")

            response = input("\nПродолжить обучение? (y/n): ")
            if response.lower() != 'y':
                return False
        else:
            print("✓ Все аннотации корректны!\n")

        return True

    def split_data(self, test_size: float = 0.15, val_size: float = 0.15, random_state: int = 42):
        """
        Разделяет данные на train/val/test
        """
        # Сначала отделяем test
        train_val, self.test_data = train_test_split(
            self.train_data,
            test_size=test_size,
            random_state=random_state
        )

        # Потом отделяем validation из оставшихся
        val_relative_size = val_size / (1 - test_size)
        self.train_data_split, self.val_data = train_test_split(
            train_val,
            test_size=val_relative_size,
            random_state=random_state
        )

        print(f"Размеры датасетов:")
        print(f"  Train: {len(self.train_data_split)} примеров")
        print(f"  Val:   {len(self.val_data)} примеров")
        print(f"  Test:  {len(self.test_data)} примеров")
        print()

    def create_model(self):
        """
        Создает пустую модель и добавляет NER
        """
        self.nlp = spacy.blank("ru")
        ner = self.nlp.add_pipe("ner")

        # Добавляем все метки
        for _, annotations in self.train_data:
            for ent in annotations.get("entities", []):
                if ent[2] not in ner.labels:
                    ner.add_label(ent[2])

        print(f"Метки NER: {ner.labels}\n")
        return ner.labels

    def evaluate(self, data: List[Tuple], verbose: bool = True) -> Dict:
        """
        Оценивает модель на заданных данных
        """
        examples = []
        for text, annotations in data:
            doc = self.nlp.make_doc(text)
            examples.append(Example.from_dict(doc, annotations))

        scorer = Scorer()

        # обязательно обновить примеры, чтобы они содержали предсказания
        for ex in examples:
            pred = self.nlp(ex.reference.text)
            ex.predicted = pred

        scores = scorer.score(examples)

        results = {
            'precision': scores.get('ents_p', 0.0),
            'recall': scores.get('ents_r', 0.0),
            'f1': scores.get('ents_f', 0.0),
            'per_type': scores.get('ents_per_type', {})
        }

        if verbose:
            print(f"  Precision: {results['precision']:.4f}")
            print(f"  Recall:    {results['recall']:.4f}")
            print(f"  F1-Score:  {results['f1']:.4f}")

        return results

    def evaluate_per_entity(self, data: List[Tuple]) -> Dict:
        """
        Детальная оценка по каждой метке
        """
        entity_stats = defaultdict(lambda: {'tp': 0, 'fp': 0, 'fn': 0})

        for text, annotations in data:
            doc = self.nlp(text)

            predicted = {(ent.start_char, ent.end_char, ent.label_)
                         for ent in doc.ents}
            expected = {(start, end, label)
                        for start, end, label in annotations["entities"]}

            for pred in predicted:
                label = pred[2]
                if pred in expected:
                    entity_stats[label]['tp'] += 1
                else:
                    entity_stats[label]['fp'] += 1

            for exp in expected:
                label = exp[2]
                if exp not in predicted:
                    entity_stats[label]['fn'] += 1

        results = {}
        for label, stats in entity_stats.items():
            tp = stats['tp']
            fp = stats['fp']
            fn = stats['fn']

            precision = tp / (tp + fp) if (tp + fp) > 0 else 0
            recall = tp / (tp + fn) if (tp + fn) > 0 else 0
            f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

            results[label] = {
                'precision': precision,
                'recall': recall,
                'f1': f1,
                'support': tp + fn
            }

        return results

    def train(self,
              n_iter: int = 100,
              dropout: float = 0.5,
              eval_every: int = 5,
              patience: int = 10,
              min_delta: float = 0.001):
        """
        Обучает модель с early stopping
        """
        print("=" * 70)
        print("НАЧАЛО ОБУЧЕНИЯ")
        print("=" * 70)

        # Создаем примеры для обучения
        train_examples = []
        for text, annotations in self.train_data_split:
            doc = self.nlp.make_doc(text)
            train_examples.append(Example.from_dict(doc, annotations))

        # Инициализация
        self.nlp.initialize(lambda: train_examples)

        # Early stopping
        patience_counter = 0

        print(f"\nПараметры обучения:")
        print(f"  Эпох: {n_iter}")
        print(f"  Dropout: {dropout}")
        print(f"  Оценка каждые: {eval_every} эпох")
        print(f"  Early stopping patience: {patience}")
        print()

        # Обучение
        for epoch in range(n_iter):
            losses = {}
            random.shuffle(train_examples)

            # Обновление модели
            self.nlp.update(train_examples, drop=dropout, losses=losses)

            # Оценка на валидации
            if epoch % eval_every == 0:
                print(f"\nEpoch {epoch}/{n_iter}")
                print(f"  Train Loss: {losses['ner']:.4f}")

                print("  Validation Metrics:")
                val_scores = self.evaluate(self.val_data, verbose=True)

                # Сохранение истории
                self.history['epoch'].append(epoch)
                self.history['train_loss'].append(losses['ner'])
                self.history['val_precision'].append(val_scores['precision'])
                self.history['val_recall'].append(val_scores['recall'])
                self.history['val_f1'].append(val_scores['f1'])

                # Early stopping
                if val_scores['f1'] > self.best_f1 + min_delta:
                    self.best_f1 = val_scores['f1']
                    patience_counter = 0

                    # Сохраняем лучшую модель
                    best_dir = self.model_dir / "best_model"
                    if best_dir.exists():
                        import shutil
                        shutil.rmtree(best_dir)
                    best_dir.mkdir(parents=True, exist_ok=True)
                    self.nlp.to_disk(best_dir)
                    self.best_model_path = best_dir

                    print(f"  ✓ Новая лучшая модель! F1: {self.best_f1:.4f}")
                else:
                    patience_counter += 1
                    print(f"  Patience: {patience_counter}/{patience}")

                    if patience_counter >= patience:
                        print(f"\n⚠️  Early stopping на эпохе {epoch}")
                        break

        print("\n" + "=" * 70)
        print("ОБУЧЕНИЕ ЗАВЕРШЕНО")
        print("=" * 70)
        print(f"Лучший F1-Score на валидации: {self.best_f1:.4f}")

        # Загружаем лучшую модель
        if self.best_model_path:
            self.nlp = spacy.load(self.best_model_path)
            print(f"Загружена лучшая модель из {self.best_model_path}")

    def test(self):
        """
        Финальное тестирование на test set
        """
        print("\n" + "=" * 70)
        print("ТЕСТИРОВАНИЕ НА TEST SET")
        print("=" * 70)

        test_scores = self.evaluate(self.test_data, verbose=True)

        # Оценка по каждой метке
        print("\n" + "-" * 70)
        print("МЕТРИКИ ПО КАЖДОЙ МЕТКЕ")
        print("-" * 70)

        per_entity_results = self.evaluate_per_entity(self.test_data)

        for label, metrics in sorted(per_entity_results.items()):
            print(f"\n{label}:")
            print(f"  Precision: {metrics['precision']:.4f}")
            print(f"  Recall:    {metrics['recall']:.4f}")
            print(f"  F1-Score:  {metrics['f1']:.4f}")
            print(f"  Support:   {metrics['support']}")

        return test_scores, per_entity_results

    def save_model(self, final: bool = True):
        """
        Сохраняет финальную модель
        """
        if final:
            output_dir = self.model_dir / "final_model"
        else:
            output_dir = self.model_dir / f"checkpoint_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        if output_dir.exists():
            import shutil
            shutil.rmtree(output_dir)

        output_dir.mkdir(parents=True, exist_ok=True)
        self.nlp.to_disk(output_dir)

        # Сохраняем историю обучения
        history_path = output_dir / "training_history.json"
        with open(history_path, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, indent=2, ensure_ascii=False)

        print(f"\n✓ Модель сохранена: {output_dir}")
        print(f"✓ История обучения: {history_path}")
        return output_dir

    def predict(self, texts: List[str], verbose: bool = True):
        """
        Предсказания на новых текстах
        """
        results = []

        for text in texts:
            doc = self.nlp(text)
            entities = [(ent.text, ent.label_, ent.start_char, ent.end_char)
                        for ent in doc.ents]
            results.append({
                'text': text,
                'entities': entities
            })

            if verbose:
                print(f"\nТекст: '{text}'")
                if entities:
                    for ent_text, label, start, end in entities:
                        print(f"  [{start}:{end}] '{ent_text}' -> {label}")
                else:
                    print("  (сущности не найдены)")

        return results

    def print_summary(self):
        """
        Печатает итоговую сводку обучения
        """
        print("\n" + "=" * 70)
        print("ИТОГОВАЯ СВОДКА")
        print("=" * 70)

        print(f"\nРазмер датасета:")
        print(f"  Train: {len(self.train_data_split)} примеров")
        print(f"  Val:   {len(self.val_data)} примеров")
        print(f"  Test:  {len(self.test_data)} примеров")

        print(f"\nЛучшие результаты на валидации:")
        if self.history['val_f1']:
            best_idx = self.history['val_f1'].index(max(self.history['val_f1']))
            print(f"  Эпоха:     {self.history['epoch'][best_idx]}")
            print(f"  Precision: {self.history['val_precision'][best_idx]:.4f}")
            print(f"  Recall:    {self.history['val_recall'][best_idx]:.4f}")
            print(f"  F1-Score:  {self.history['val_f1'][best_idx]:.4f}")

        print(f"\nМодель сохранена в: {self.model_dir / 'final_model'}")

    # def fine_tune(self,
    #               new_data: List[Tuple],
    #               n_iter: int = 20,
    #               dropout: float = 0.2,
    #               mix_old_ratio: float = 0.5):
    #     """
    #     Точечное дообучение модели на новых примерах.
    #
    #     new_data     — новые размеченные примеры [(text, {"entities": [...]})]
    #     n_iter       — сколько эпох дообучать
    #     dropout      — дропаут (можно поменьше, чем при первичном обучении)
    #     mix_old_ratio — доля старых примеров в смеси (0..1)
    #     """
    #     print("=" * 70)
    #     print("ДОПОЛНИТЕЛЬНОЕ ОБУЧЕНИЕ (FINE-TUNING)")
    #     print("=" * 70)
    #
    #     # 1. Опционально мешаем новые примеры со старыми, чтобы не забыть старое
    #     train_pool = list(new_data)
    #
    #     if mix_old_ratio > 0 and hasattr(self, "train_data_split"):
    #         import random
    #         old_count = int(len(new_data) * mix_old_ratio)
    #         old_samples = random.sample(
    #             self.train_data_split,
    #             k=min(old_count, len(self.train_data_split))
    #         )
    #         train_pool.extend(old_samples)
    #
    #     # 2. Собираем Example'ы
    #     examples = []
    #     for text, annotations in train_pool:
    #         doc = self.nlp.make_doc(text)
    #         examples.append(Example.from_dict(doc, annotations))
    #
    #     # 3. Возобновляем обучение
    #     optimizer = self.nlp.resume_training()
    #
    #     print(f"Всего примеров для дообучения: {len(examples)}")
    #     print(f"Эпох: {n_iter}, dropout: {dropout}\n")
    #
    #     for epoch in range(n_iter):
    #         import random
    #         random.shuffle(examples)
    #         losses = {}
    #         # Можно батчевать, но для простоты — всё сразу
    #         self.nlp.update(
    #             examples,
    #             sgd=optimizer,
    #             drop=dropout,
    #             losses=losses
    #         )
    #         print(f"Epoch {epoch + 1}/{n_iter}  Loss: {losses.get('ner', 0):.4f}")
    #
    #     print("\n✓ Дообучение завершено")

    @classmethod
    def load_from_path(cls, model_dir: str | Path):
        """
        Загрузка уже обученной модели с диска.

        Использование:
            trainer = NERTrainer.load_from_path("spacy_geo_model/final_model")
            trainer.predict(["Москва, Тверская, 10"])
        """
        model_dir = Path(model_dir)

        if not model_dir.exists():
            raise ValueError(f"Модель по пути {model_dir} не найдена")

        # Загружаем spaCy-модель
        nlp = spacy.load(model_dir)

        # Создаем "пустой" тренер, но с правильным model_dir
        trainer = cls(train_data=[], model_dir=str(model_dir))
        trainer.nlp = nlp

        # Чтобы не словить AttributeError в методах, которые ждут эти атрибуты
        trainer.train_data_split = []
        trainer.val_data = []
        trainer.test_data = []

        # best_model_path и best_f1 можно не трогать, но на всякий случай:
        trainer.best_model_path = model_dir
        trainer.best_f1 = 0.0

        return trainer

if __name__ == "__main__":
    from pathlib import Path

    # грузим финальную модель
    trainer = NERTrainer.load_from_path("spacy_geo_model/final_model")

    # предсказание на новых строках
    result = trainer.predict([
        "г. Москва, ул. Пушкина, д. 10",
        "Москва, Тверская 7"
    ], verbose=False)

    print(result)