import json
import re

import pymorphy3


class Normalizer:
    def __init__(self):
        self.morph = pymorphy3.MorphAnalyzer()
        with open("./resources/contractions.json", 'r') as f:
            self.contractions = json.load(f)

    def _clean_token(self, token: str) -> str:
        # Разрешаем буквы, цифры и -, \, /
        return re.sub(r"[^0-9A-Za-zА-Яа-яёЁ\\/\-]", " ", token)

    def replacement_contractions(self, text: str) -> str:
        for contraction, full_word in self.contractions.items():
            pattern = rf"(?<!\S){re.escape(contraction)}(?!\S)"
            text = re.sub(pattern, f"{full_word} ", text)
        return text

    def normalize_sentence(self, text: str) -> str:
        text = text.lower()
        text = self._clean_token(text).replace("  ", " ")
        text = self.replacement_contractions(text)
        tokens = re.findall(r"\w+|[^\w\s]+", text, flags=re.UNICODE)

        normalized_tokens = []

        for token in tokens:
            cleaned = self._clean_token(token)
            cleaned = cleaned
            if not cleaned:
                continue

            # Если есть цифра — НЕ нормализуем через pymorphy2
            if any(ch.isdigit() for ch in cleaned):
                normalized_tokens.append(cleaned)
                continue

            # Иначе нормализуем
            if any(ch.isalpha() for ch in cleaned):
                parsed = self.morph.parse(cleaned)[0]
                norm = parsed.normal_form
                normalized_tokens.append(norm)
            else:
                normalized_tokens.append(cleaned)

        # Склейка
        result = ""
        for x, tok in enumerate(normalized_tokens):
            if not result:
                result += tok
            else:
                if tok in "\/-":
                    result += tok
                elif normalized_tokens[x-1] in "\/-":
                    result += tok
                else:
                    result += " " + tok
        return result.replace("  ", " ")

if __name__ == "__main__":
    n = Normalizer()
    a = ['СПб, Невский проспект 88', 'Екатеринбург ул.Ленина 45 корп.1', 'Новосибирск, Красный пр-т, 35', '630102, Новосибирск, ул. Кирова, д.86', 'Казань, Баумана 15', 'Нижний Новгород, Большая Покровская, 28', 'Самара, ул. Ленинградская, д.55 кв.12', 'Омск ул.Маркса 41', 'Челябинск, проспект Ленина, 23А', 'Ростов-на-Дону, Большая Садовая ул., 115', 'Уфа, ул.Ленина, д.151', 'Красноярск, пр-т Мира 88', 'Пермь, ул. Комсомольская 45', 'Воронеж, Кольцовская улица, 35', 'Волгоград, пр. Ленина, д.62', 'Краснодар ул.Красная 176', 'Саратов, Московская ул., 34', 'Тюмень, ул.Республики 61', 'Тольятти, Автозаводское шоссе, 15', 'г.Ижевск, ул.Пушкинская, 268', 'Барнаул, пр-т Ленина, д.99', 'Ульяновск ул.Гончарова 25', 'Иркутск, ул. Карла Маркса, 18', 'Хабаровск, ул.Муравьева-Амурского, 23', 'Ярославль, Которосльная наб., 44', 'Владивосток ул.Светланская 47', 'Махачкала, пр-т Расула Гамзатова, 55', 'Томск, пр. Ленина, 36', 'Оренбург, ул.Советская, д.8', 'Кемерово ул.Весенняя 20', 'Новокузнецк, пр.Металлургов, 48', 'Рязань, ул. Почтовая, 61', 'Астрахань, ул.Кирова 18', 'Пенза, Московская ул., д.83', 'Липецк ул.Ленина 27', 'Киров, ул.Спасская, 41', 'Чебоксары, Московский пр-т, 19', 'Калининград, пр-т Мира, д.91', 'Брянск, Красноармейская ул., 100', 'Курск ул.Ленина 69', 'Иваново, пр-т Ленина, 109', 'Магнитогорск, ул.Гагарина, 15', 'Тверь, Советская ул., д.34', 'Ставрополь ул.Мира 285', 'Нижний Тагил, пр.Ленина, 1', 'Белгород, Народный бульвар, 89', 'Архангельск, Троицкий пр-т, 61', 'Владимир, ул.Большая Московская, 19', 'Сочи ул.Навагинская 12', 'Курган, ул.Гоголя, 56', 'Смоленск, ул.Большая Советская, 18/20', 'Калуга, ул.Кирова, д.29', 'Чита ул.Ленина 85', 'Орел, Московская ул., 31', 'Волжский, ул.Мира, 75', 'Череповец, Советский пр-т, 88', 'Владикавказ ул.Мира 17']
    for i in a:
        print(i, ";", n.normalize_sentence(i))
