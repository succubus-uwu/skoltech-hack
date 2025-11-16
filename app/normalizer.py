import json
import re
from typing import Dict, Any, Tuple, Optional, List

import pymorphy3


class Normalizer:
    def __init__(self, contractions_path: str):
        self.MARKER_KS = r'(?:(?:[кkKК])|(?:[сcCС]))'
        self.OTHER_MARKERS = r'(?:вл|стр|ст|кв|под|п/п)'
        self.NUM_WITH_SUFFIX = r'(?P<num>\d+)(?P<letter>[A-Za-zА-Яа-яЁё0-9\-]{0,3})'
        self.morph = pymorphy3.MorphAnalyzer()
        with open(contractions_path, 'r') as f:
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

    def _normalize_token(self, token: str) -> str:
        return token.replace('.', '').replace(',', '').strip()

    def _split_number_letter(self, value: str) -> Tuple[Optional[str], Optional[str]]:
        m = re.match(self.NUM_WITH_SUFFIX, value)
        if not m:
            return None, None
        return m.group("num"), m.group("letter") or None

    def _parse_multi_fraction(self, token: str) -> Optional[List[str]]:
        """
        Разбирает цепочки вида:
            1/13/6
            10/5/2/7
        Возвращает список: ["1", "13", "6"]
        Если не подходит под формат — возвращает None.
        """
        if "/" not in token:
            return None
        parts = token.split("/")
        for p in parts:
            if not re.match(r'^\d+[A-Za-zА-Яа-яЁё\-]{0,3}$', p):
                return None
        return parts

    def parse_address_suffix(self, text: str) -> Dict[str, Any]:
        original = text
        text = self._normalize_token(text)

        result = {
            "raw": original,
            "primary": None,
            "primary_chain": [],
            "range": None,
            "parts": [],
            "free": []
        }

        if not text:
            return result

        m_start_multi = re.match(
            r'^(\d+[A-Za-zА-Яа-яЁё\-]{0,3}(?:/\d+[A-Za-zА-Яа-яЁё\-]{0,3})+)(?:\s|$)',
            text
        )

        if m_start_multi:
            chain = self._parse_multi_fraction(m_start_multi.group(1))
            if chain:
                result["primary_chain"] = chain
                result["primary"] = chain[0]
                text = text[m_start_multi.end():].strip()

        else:
            primary_match = re.match(
                r'^(?P<p1>\d+[A-Za-zА-Яа-яЁё\-]{0,3})(?:/(?P<p2>\d+[A-Za-zА-Яа-яЁё\-]{0,3}))?(?:\s|$)',
                text
            )
            if primary_match:
                p1 = primary_match.group("p1")
                p2 = primary_match.group("p2")

                if p2:
                    result["primary_chain"] = [p1, p2]
                else:
                    result["primary_chain"] = [p1]

                result["primary"] = p1
                text = text[primary_match.end():].strip()

        if result["primary"] and "-" in result["primary"]:
            a, b = result["primary"].split("-", 1)
            result["range"] = (a, b)

        tokens = [tok for tok in re.split(r'\s+', text) if tok]

        i = 0
        while i < len(tokens):
            raw_tok = tokens[i]
            tok = self._normalize_token(raw_tok)

            chain = self._parse_multi_fraction(tok)
            if chain:
                if not result["primary_chain"]:
                    result["primary_chain"] = chain
                    result["primary"] = chain[0]
                else:
                    result["free"].append(tok)
                i += 1
                continue

            m_ks = re.match(
                rf'^(?P<marker>{self.MARKER_KS})(?P<body>\d+[A-Za-zА-Яа-яЁё\-]{{0,3}})$',
                tok,
                re.I
            )
            if m_ks:
                marker = m_ks.group("marker")
                body = m_ks.group("body")
                typ = "к" if re.match(r'[кkKК]', marker, re.I) else "с"
                num, letter = self._split_number_letter(body)
                result["parts"].append({
                    "type": typ,
                    "num": num,
                    "letter": letter,
                    "raw": raw_tok
                })
                i += 1
                continue

            if re.match(rf'^(?:{self.MARKER_KS}|{self.OTHER_MARKERS})$', tok, re.I) and i + 1 < len(tokens):
                next_tok = self._normalize_token(tokens[i + 1])
                num, letter = self._split_number_letter(next_tok)

                if num is not None:
                    mk = tok.lower()
                    if re.match(r'[кkKК]', mk, re.I):
                        typ = "к"
                    elif re.match(r'[сcCС]', mk, re.I):
                        typ = "с"
                    else:
                        typ = mk

                    if mk == "вл":
                        result["raw"] = raw_tok + " " + tokens[i + 1]
                        result["primary"] = num
                        result["letter"] = letter
                        i += 2
                        continue

                    result["parts"].append({
                        "type": typ,
                        "num": num,
                        "letter": letter,
                        "raw": raw_tok + " " + tokens[i + 1]
                    })
                    i += 2
                    continue

            m_other = re.match(
                rf'^(?P<marker>{self.OTHER_MARKERS})(?P<body>\d*[A-Za-zА-Яа-яЁё\-]*)$',
                tok,
                re.I
            )
            if m_other:
                mk = m_other.group("marker").lower()
                body = m_other.group("body")
                num, letter = self._split_number_letter(body) if body else (None, None)

                if mk == "вл":
                    result["raw"] = raw_tok
                    result["primary"] = num
                    result["letter"] = letter
                    i += 1
                    continue

                result["parts"].append({
                    "type": mk,
                    "num": num,
                    "letter": letter,
                    "raw": raw_tok
                })
                i += 1
                continue

            m_range = re.match(r'^(?P<a>\d+)-(?P<b>\d+)$', tok)
            if m_range:
                result["range"] = (m_range.group("a"), m_range.group("b"))
                i += 1
                continue

            num, letter = self._split_number_letter(tok)
            if num is not None:
                result["free"].append(tok)
                i += 1
                continue

            result["free"].append(tok)
            i += 1

        if "primary" in result and result["primary"] is not None:
            upd_primary = ""
            for i in result["primary"]:
                if i.isdigit():
                    upd_primary += i
            result["primary"] = upd_primary
        return result

if __name__ == "__main__":
    n = Normalizer(contractions_path="../resources/contractions.json")
    a = ['СПб, Невский проспект 88', 'Екатеринбург ул.Ленина 45 корп.1', 'Новосибирск, Красный пр-т, 35', '630102, Новосибирск, ул. Кирова, д.86', 'Казань, Баумана 15', 'Нижний Новгород, Большая Покровская, 28', 'Самара, ул. Ленинградская, д.55 кв.12', 'Омск ул.Маркса 41', 'Челябинск, проспект Ленина, 23А', 'Ростов-на-Дону, Большая Садовая ул., 115', 'Уфа, ул.Ленина, д.151', 'Красноярск, пр-т Мира 88', 'Пермь, ул. Комсомольская 45', 'Воронеж, Кольцовская улица, 35', 'Волгоград, пр. Ленина, д.62', 'Краснодар ул.Красная 176', 'Саратов, Московская ул., 34', 'Тюмень, ул.Республики 61', 'Тольятти, Автозаводское шоссе, 15', 'г.Ижевск, ул.Пушкинская, 268', 'Барнаул, пр-т Ленина, д.99', 'Ульяновск ул.Гончарова 25', 'Иркутск, ул. Карла Маркса, 18', 'Хабаровск, ул.Муравьева-Амурского, 23', 'Ярославль, Которосльная наб., 44', 'Владивосток ул.Светланская 47', 'Махачкала, пр-т Расула Гамзатова, 55', 'Томск, пр. Ленина, 36', 'Оренбург, ул.Советская, д.8', 'Кемерово ул.Весенняя 20', 'Новокузнецк, пр.Металлургов, 48', 'Рязань, ул. Почтовая, 61', 'Астрахань, ул.Кирова 18', 'Пенза, Московская ул., д.83', 'Липецк ул.Ленина 27', 'Киров, ул.Спасская, 41', 'Чебоксары, Московский пр-т, 19', 'Калининград, пр-т Мира, д.91', 'Брянск, Красноармейская ул., 100', 'Курск ул.Ленина 69', 'Иваново, пр-т Ленина, 109', 'Магнитогорск, ул.Гагарина, 15', 'Тверь, Советская ул., д.34', 'Ставрополь ул.Мира 285', 'Нижний Тагил, пр.Ленина, 1', 'Белгород, Народный бульвар, 89', 'Архангельск, Троицкий пр-т, 61', 'Владимир, ул.Большая Московская, 19', 'Сочи ул.Навагинская 12', 'Курган, ул.Гоголя, 56', 'Смоленск, ул.Большая Советская, 18/20', 'Калуга, ул.Кирова, д.29', 'Чита ул.Ленина 85', 'Орел, Московская ул., 31', 'Волжский, ул.Мира, 75', 'Череповец, Советский пр-т, 88', 'Владикавказ ул.Мира 17']
    for i in a:
        print(i, ";", n.normalize_sentence(i))
