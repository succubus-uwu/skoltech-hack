import uuid
import asyncio
from typing import List, Tuple

import spacy
from anthropic import AsyncAnthropic
from spacy.tokens import Doc

from normalizer import Normalizer

nlp = spacy.blank("ru")


class AddressGenerator:
    def __init__(
            self,
            client: AsyncAnthropic,
            normalizer: Normalizer,
            count: int = 10
    ):
        self.client = client
        self.normalizer = normalizer
        self.count = count

    def _generate_salt(self) -> str:
        return str(uuid.uuid4())

    async def generate_address(self, salt: str = None) -> List[str]:
        if salt is None:
            salt = self._generate_salt()

        response = await self.client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=20000,
            temperature=0.5,
            system="""
            
Сгенерируй разнообразные российские адреса зданий в том виде, в котором их могут писать обычные пользователи. 

Требования:

addr:street - название улицы, проспекта, бульвара и т.д.
addr:housenumber - номер дома/домов, владения (вл), корпуса (к), строения (с), бывают с литерой на конце
addr:postcode - почтовый индекс (6 цифр)

Всего может быть 10 разных перестановок:
- 1 addr:street -> addr:housenumber
- 2 addr:housenumber -> addr:street 
- 3 addr:postcode -> addr:housenumber
- 4 addr:housenumber -> addr:postcode
- 5 addr:postcode -> addr:street -> addr:housenumber
- 6 addr:postcode -> addr:housenumber -> addr:street
- 7 addr:street -> addr:postcode -> addr:housenumber
- 8 addr:street -> addr:housenumber -> addr:postcode
- 9 addr:housenumber -> addr:postcode -> addr:street
- 10 addr:housenumber -> addr:street -> addr:postcode
- Только на русском языке

Примеры допустимых форматов:
- г. Москва, вл8 к1, ул. Тверская
- СПб, Невский пр-т к809А
- Москва, 10 к2 улица Ленина
- Москва, 10 улица Ленина
- Екатеринбург, ул.Малышева, 45-57
- 125167, Москва, 95 к11, Ленинградский проспект
- Новосибирск, Красный проспект 100/2
- Казань ул. Баумана 88 к3 с3
- пр. Мира 84 с1, Мск
- Санкт-Петербург, наб. реки Мойки, 12-17
- Нижний Новгород, 35, улица Большая Покровская

Сгенерируй адреса в произвольном, но естественном виде, как это делают реальные пользователи.""",
            messages=[{
                "role": "user",
                "content": f"Сгенерируй {self.count} различных российских адресов. Каждый адрес с новой строки."
            }],
            extra_headers={"X-Stochastic-Param": salt}
        )

        addresses_text = response.content[0].text
        addresses = [
            addr.strip()
            for addr in addresses_text.split('\n')
            if addr.strip() and not addr.strip().startswith(('#', '-', '•'))
        ]

        return addresses[:self.count]

    async def generate_addresses_batch(
            self,
            batch_count: int = 5,
            concurrency_limit: int = 3
    ) -> List[str]:
        """
        Генерирует несколько батчей адресов с ограничением на параллельное выполнение
        """
        semaphore = asyncio.Semaphore(concurrency_limit)

        async def generate_with_semaphore():
            async with semaphore:
                return await self.generate_address()

        # Создаем задачи для генерации батчей
        tasks = [generate_with_semaphore() for _ in range(batch_count)]

        # Используем gather для параллельного выполнения
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Обрабатываем результаты
        all_addresses = []
        for result in results:
            if isinstance(result, Exception):
                print(f"Ошибка при генерации адресов: {result}")
                continue
            all_addresses.extend(result)

        return all_addresses


class AddressClassifier:
    def __init__(
            self,
            client: AsyncAnthropic,
            normalizer: Normalizer,
            concurrency_limit: int = 5
    ):
        self.client = client
        self.normalizer = normalizer
        self.concurrency_limit = concurrency_limit
        self.semaphore = asyncio.Semaphore(concurrency_limit)
        self.entity_types = {
            "addr:street": "название улицы, проспекта, бульвара и т.д.",
            "addr:postcode": "почтовый индекс (6 цифр)",
            "addr:housenumber": "номер дома, корпуса, строения"
        }

    def _get_classification_prompt(
            self,
            text: str,
            tokens_with_pos: Doc
    ) -> str:
        tokens_info = [
            f"'{token.text}' [{token.idx}:{token.idx + len(token.text)}]"
            for token in tokens_with_pos
        ]
        tokens_str = "\n".join(tokens_info)

        return f"""Ты - эксперт по извлечению сущностей из русских адресов. Проанализируй текст и найди все адресные элементы.

Текст: "{text}"

Токены с позициями:
{tokens_str}

Доступные типы сущностей:
- "addr:street": название улицы, проспекта, бульвара и т.д.
- "addr:postcode": почтовый индекс (6 цифр)
- "addr:housenumber": номер дома, корпуса, строения
- прочие случаи не классифицировать и пропускать токен

Инструкции:
1. Анализируй только указанные токены
2. Определи к какому типу сущности относится каждый токен
3. Если токен не относится к адресным сущностям - не включай его
4. Для "addr:street" включай как названия улиц, так и их типы (ул, пр, и т.д.)
5. Для "addr:housenumber" включай только числовые обозначения домов
6. При разметке учитывай многотокенность сущности - ты готовишь тестовый сет для NER. Таким образом сущность должна содержать все входящие в неё токены и пробелы (начинаться со стартового индекса первого токена и заканчиваться финальным индексом поелсднего токена)

Формат ответа - только JSON:
{{
  "entities": [
    [start, end, "ENTITY_TYPE"],
    [start, end, "ENTITY_TYPE"],
    ...
  ]
}}

Примеры:

Текст: "москва ул арбат д 28 кв 15"
Токены: 
'москва' [0:6]
'ул' [7:9] 
'арбат' [10:15]
'д' [16:17]
'28' [18:20]
'кв' [21:23]
'15' [24:26]

Ответ: {{
  "entities": [
    [7, 15, "addr:street"],
    [18, 20, "addr:housenumber"]
  ]
}}

Текст: "125167 москва пр мира дом 25 корп 2"
Токены:
'125167' [0:6]
'москва' [7:13]
'пр' [14:16]
'мира' [17:21]
'дом' [22:25]
'25' [26:28]
'корп' [29:33]
'2' [34:35]

Ответ: {{
  "entities": [
    [0, 6, "addr:postcode"],
    [14, 21, "addr:street"],
    [26, 35, "addr:housenumber"]
  ]
}}

Теперь проанализируй текст и верни результат в указанном формате:"""

    async def classify_address(
            self,
            text: str
    ) -> dict[str, List[Tuple[int, int, str]]]:
        tokens_with_pos = nlp.make_doc(text)

        response = await self.client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=20000,
            temperature=0.1,
            system="Ты - эксперт по извлечению сущностей из русских адресов. Отвечай только в формате JSON.",
            messages=[{
                "role": "user",
                "content": self._get_classification_prompt(text, tokens_with_pos)
            }]
        )

        result_text = response.content[0].text.lstrip('```json').rstrip('```')

        import json
        result = json.loads(result_text)

        entities = [
            (entity[0], entity[1], entity[2])
            for entity in result.get("entities", [])
        ]

        return {"entities": entities}

    async def normalize_and_classify(
            self,
            text: str
    ) -> Tuple[str, dict[str, List[Tuple[int, int, str]]]]:
        """Нормализация и классификация с использованием семафора"""
        async with self.semaphore:
            normalized_text = self.normalizer.normalize_sentence(text)
            classification_result = await self.classify_address(normalized_text)
            return normalized_text, classification_result

    async def classify_addresses_batch(
            self,
            addresses: List[str]
    ) -> List[Tuple[str, dict]]:
        """
        Классифицирует список адресов параллельно с ограничением на параллелизм
        """
        # Создаем задачи для классификации
        tasks = [self.normalize_and_classify(address) for address in addresses]

        # Используем gather для параллельного выполнения
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Обрабатываем результаты
        processed_results = []
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                print(f"Ошибка при обработке адреса '{addresses[i]}': {result}")
                processed_results.append((addresses[i], {"entities": []}))
            else:
                processed_results.append(result)

        return processed_results
