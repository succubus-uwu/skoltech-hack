import json

import numpy as np
import osmium
import pandas as pd

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

from app.normalizer import Normalizer


class Finder:
    def __init__(self, data_path: str, normalizer: Normalizer):
        # self.relations = self._get_relations()
        df = pd.read_csv(data_path)
        self.data_by_city = self._get_data_by_city(df)
        self.data_by_street = self._get_data_by_street(df)
        self.data_by_postcode = self._get_data_by_postcode(df)
        self.normalizer = normalizer

    def _get_data_by_city(self, df):
        data_by_city = {}
        for i in df.iterrows():
            try:
                addr = eval(i[1]["addr"])
                coords = eval(i[1]["coords"])
                if "addr:city" not in addr:
                    continue
                if addr["addr:city"] not in data_by_city:
                    data_by_city[addr["addr:city"]] = []

                cur_data = []
                if "addr:street" not in addr:
                    cur_data += [None]
                else:
                    cur_data = [addr["addr:street"]]
                if "addr:housenumber" not in addr:
                    cur_data += [None]
                else:
                    cur_data += [addr["addr:housenumber"]]
                if "addr:postcode" not in addr:
                    cur_data += [None]
                else:
                    cur_data += [addr["addr:postcode"]]
                cur_data += [coords]

                data_by_city[addr["addr:city"]].append(cur_data)


            except:
                continue

        return data_by_city

    def _get_data_by_street(self, df):
        data_by_street = {}
        for i in df.iterrows():
            try:
                addr = eval(i[1]["addr"])
                coords = eval(i[1]["coords"])
                if "addr:street_normalized" not in addr:
                    continue
                if "addr:street" not in addr:
                    continue
                if addr["addr:street_normalized"] not in data_by_street:
                    data_by_street[addr["addr:street_normalized"]] = []

                cur_data = [addr["addr:street"]]
                if "addr:housenumber" not in addr:
                    cur_data += [None]
                else:
                    cur_data += [addr["addr:housenumber"]]
                if "addr:postcode" not in addr:
                    cur_data += [None]
                else:
                    cur_data += [addr["addr:postcode"]]
                if "addr:city" not in addr:
                    cur_data += [None]
                else:
                    cur_data += [addr["addr:city"]]
                cur_data += [coords]

                data_by_street[addr["addr:street_normalized"]].append(cur_data)


            except:
                continue

        return data_by_street

    def _get_data_by_postcode(self, df):
        data_by_postcode = {}
        for i in df.iterrows():
            try:
                addr = eval(i[1]["addr"])
                coords = eval(i[1]["coords"])
                if "addr:postcode" not in addr:
                    continue
                if addr["addr:postcode"] not in data_by_postcode:
                    data_by_postcode[addr["addr:postcode"]] = []

                cur_data = []
                if "addr:street" not in addr:
                    cur_data += [None]
                else:
                    cur_data = [addr["addr:street"]]
                if "addr:housenumber" not in addr:
                    cur_data += [None]
                else:
                    cur_data += [addr["addr:housenumber"]]
                if "addr:city" not in addr:
                    cur_data += [None]
                else:
                    cur_data += [addr["addr:city"]]
                cur_data += [coords]

                data_by_postcode[addr["addr:postcode"]].append(cur_data)


            except:
                continue
        return data_by_postcode

    def _get_relations(self_f):
        class RelationIndexHandler(osmium.SimpleHandler):
            """
            Первый проход:
            собираем только relation’ы зданий в Москве
            и список нужных way_id, чтобы потом вытащить их координаты.
            """

            def __init__(self):
                super().__init__()
                self.access_keys = {"addr:city", "addr:street", "addr:postcode", "addr:housenumber"}
                self.normalizer = self_f.normalizer
                self.rows_raw = {}  # rel_id -> {"addr": {...}, "way_ids": [...]}
                self.needed_way_ids = set()
                self._street_cache = {}

            def _normalize_street(self, value: str) -> str:
                if value in self._street_cache:
                    return self._street_cache[value]
                norm = self.normalizer.normalize_sentence(value)
                self._street_cache[value] = norm
                return norm

            def relation(self, r):
                # интересуют только здания
                if "building" not in r.tags:
                    return

                if "addr:city" not in r.tags:
                    return

                # фильтр по Москве (если pbf уже вырезан — можно убрать)
                if not (r.tags.get("addr:city").lower() == "москва" or
                        r.tags.get("addr:city").lower() == "moscow" or
                        r.tags.get("addr:city").lower() == "мск" or
                        r.tags.get("addr:city").lower() == "msc"):
                    return

                addr_tags = {}
                for key, value in r.tags:
                    if key.startswith("addr:") and key in self.access_keys:
                        if key == "addr:street":
                            addr_tags[f"{key}_normalized"] = self._normalize_street(value)
                            addr_tags[key] = value
                        else:
                            addr_tags[key] = value

                if not addr_tags:
                    return

                way_ids = [m.ref for m in r.members if m.type == "w"]
                if not way_ids:
                    return

                rel_id = r.id
                self.rows_raw[rel_id] = {
                    "addr": addr_tags,
                    "way_ids": way_ids,
                }
                self.needed_way_ids.update(way_ids)

        class WayHandler(osmium.SimpleHandler):
            """
            Второй проход:
            1) по needed_way_ids собираем координаты для relation-ов
            2) параллельно собираем обычные way-здания с адресами
            """

            def __init__(self, needed_way_ids):
                super().__init__()
                self.needed_way_ids = needed_way_ids

                self.way_coords = {}  # way_id -> [(lat, lon), ...]
                self.rows_buildings = []

                self.access_keys = {"addr:city", "addr:street", "addr:postcode", "addr:housenumber"}
                self.normalizer = self_f.normalizer
                self._street_cache = {}

            def _normalize_street(self, value: str) -> str:
                if value in self._street_cache:
                    return self._street_cache[value]
                norm = self.normalizer.normalize_sentence(value)
                self._street_cache[value] = norm
                return norm

            def way(self, w):
                # 1) если way нужен как часть relation — сохраняем его координаты
                if w.id in self.needed_way_ids:
                    coords_rel = []
                    for n in w.nodes:
                        if n.location.valid():
                            coords_rel.append((n.location.lat, n.location.lon))
                    if coords_rel:
                        self.way_coords[w.id] = coords_rel

                # 2) отдельно собираем ВСЕ здания-ways с адресами
                if "building" not in w.tags:
                    return

                if "addr:city" not in w.tags:
                    return

                if not (w.tags.get("addr:city").lower() == "москва" or
                        w.tags.get("addr:city").lower() == "moscow" or
                        w.tags.get("addr:city").lower() == "мск" or
                        w.tags.get("addr:city").lower() == "msc"):
                    return

                addr_tags = {}
                for key in self.access_keys:
                    val = w.tags.get(key)
                    if not val:
                        continue

                    if key == "addr:street":
                        addr_tags[f"{key}_normalized"] = self._normalize_street(val)
                        addr_tags[key] = val
                    else:
                        addr_tags[key] = val

                if not addr_tags:
                    return

                coords = []
                for n in w.nodes:
                    if n.location.valid():
                        coords.append((n.location.lat, n.location.lon))

                if not coords:
                    return

                self.rows_buildings.append(
                    {
                        "id": w.id,  # way id
                        "addr": addr_tags,
                        "coords": coords,
                    }
                )

        class NodeAddrHandler(osmium.SimpleHandler):
            """
            Третий проход:
            собираем адресные точки (node с addr:* в Москве).
            Это не здания, а отдельные адресные объекты, но
            сильно увеличивает покрытие.
            """

            def __init__(self):
                super().__init__()
                self.rows_nodes = []
                self.access_keys = {"addr:city", "addr:street", "addr:postcode", "addr:housenumber"}
                self.normalizer = self_f.normalizer
                self._street_cache = {}

            def _normalize_street(self, value: str) -> str:
                if value in self._street_cache:
                    return self._street_cache[value]
                norm = self.normalizer.normalize_sentence(value)
                self._street_cache[value] = norm
                return norm

            def node(self, n):
                if "addr:city" not in n.tags:
                    return

                # фильтр по Москве
                if not (n.tags.get("addr:city").lower() == "москва" or
                        n.tags.get("addr:city").lower() == "moscow" or
                        n.tags.get("addr:city").lower() == "мск" or
                        n.tags.get("addr:city").lower() == "msc"):
                    return

                addr_tags = {}
                for key in self.access_keys:
                    val = n.tags.get(key)
                    if not val:
                        continue
                    if key == "addr:street":
                        addr_tags[f"{key}_normalized"] = self._normalize_street(val)
                        addr_tags[key] = val
                    else:
                        addr_tags[key] = val

                if not addr_tags:
                    return

                if not n.location.valid():
                    return

                coord = (n.location.lat, n.location.lon)

                self.rows_nodes.append(
                    {
                        "id": f"n{n.id}",  # пометим как node
                        "addr": addr_tags,
                        "coords": [coord],
                    }
                )

        pbf_path = "data.osm.pbf"

        # 1-й проход: relation’ы
        rel_handler = RelationIndexHandler()
        rel_handler.apply_file(pbf_path)
        print("КОНЕЦ 1 ШАГА (relations)")

        # 2-й проход: way’и — и координаты для relation, и отдельные здания-ways
        way_handler = WayHandler(rel_handler.needed_way_ids)
        way_handler.apply_file(pbf_path, locations=True)
        print("КОНЕЦ 2 ШАГА (ways)")

        # 3-й проход: адресные точки (nodes)
        node_handler = NodeAddrHandler()
        node_handler.apply_file(pbf_path, locations=True)
        print("КОНЕЦ 3 ШАГА (nodes)")

        rows = []

        # relation-ы с координатами
        for rel_id, data in rel_handler.rows_raw.items():
            addr_tags = data["addr"]
            way_ids = data["way_ids"]

            coords = []
            for wid in way_ids:
                wc = way_handler.way_coords.get(wid)
                if wc:
                    coords.extend(wc)

            if not coords:
                continue

            rows.append(
                {
                    "id": f"r{rel_id}",  # пометим как relation
                    "addr": addr_tags,
                    "coords": coords,
                }
            )

        # здания-ways
        rows.extend(
            {
                "id": f"w{row['id']}",  # помечаем префиксом
                "addr": row["addr"],
                "coords": row["coords"],
            }
            for row in way_handler.rows_buildings
        )

        # адресные nodes
        rows.extend(node_handler.rows_nodes)

        return rows

    def centroid_mean(self, coords):
        """
        coords — список (lat, lon)
        возвращает (centroid_lat, centroid_lon)
        """
        if not coords:
            return None

        lat_sum = 0.0
        lon_sum = 0.0

        for lat, lon in coords:
            lat_sum += lat
            lon_sum += lon

        n = len(coords)
        return lat_sum / n, lon_sum / n

    def get_most_similar(self, user_input: dict):
        def _compare_parts(parts, user_parts):
            similar_parts = []
            for part in parts:
                for user_part in user_parts:
                    if part["type"] != user_part["type"]:
                        continue
                    if part["num"] != user_part["num"]:
                        continue
                    if part["letter"] != user_part["letter"]:
                        continue
                    similar_parts.append((part, user_part,))
            return similar_parts

        similar_cities = []
        if user_input["city"] is not None:
            for city in self.data_by_city:
                rate = fuzz.token_set_ratio(city, user_input["city"])
                if rate >= 80:
                    similar_cities.append(city)
            if len(similar_cities) == 0:
                return []

        if user_input["street"] is not None and user_input["housenumber"] is not None:
            similar_streets = []
            for street_norm in self.data_by_street:
                rate = fuzz.token_set_ratio(street_norm, user_input["street"])
                if rate >= 95:
                    similar_streets.append(street_norm)
            similar_address = []
            for street_norm in similar_streets:
                for option in self.data_by_street[street_norm]:
                    if option[1] is None:
                        continue
                    num = self.normalizer.parse_address_suffix(option[1])
                    user_num = user_input["housenumber"]
                    if num["primary"] is not None and user_num["primary"] is not None:
                        delt = abs(int(num["primary"]) - int(user_num["primary"]))
                        if delt == 0:
                            similar_parts = _compare_parts(num["parts"], user_num["parts"])
                            if len(similar_parts) != 0:
                                similar_address.append(option)
                    elif num["range"] is not None and user_num["range"] is not None:
                        if num["range"] == user_num["range"]:
                            similar_parts = _compare_parts(num["parts"], user_num["parts"])
                            if len(similar_parts) != 0:
                                similar_address.append(option)
            if len(similar_address) != 0:
                return similar_address
    
            for street_norm in similar_streets:
                for option in self.data_by_street[street_norm]:
                    if option[1] is None:
                        continue
                    num = self.normalizer.parse_address_suffix(option[1])
                    user_num = user_input["housenumber"]
                    if num["primary"] is not None and user_num["primary"] is not None:
                        delt = abs(int(num["primary"]) - int(user_num["primary"]))
                        if delt == 0:
                            similar_address.append(option)
                    elif num["range"] is not None and user_num["range"] is not None:
                        if num["range"] == user_num["range"]:
                            similar_address.append(option)
            if len(similar_address) != 0:
                return similar_address
    
            for street_norm in similar_streets:
                for option in self.data_by_street[street_norm]:
                    if option[1] is None:
                        continue
                    num = self.normalizer.parse_address_suffix(option[1])
                    user_num = user_input["housenumber"]
                    if num["primary"] is not None and user_num["primary"] is not None:
                        delt = abs(int(num["primary"]) - int(user_num["primary"]))
                        if delt <= 5:
                            similar_address.append(option)
    
            return similar_address

        if user_input["street"] is not None:
            similar_address = []
            for street_norm in self.data_by_street:
                rate = fuzz.token_set_ratio(street_norm, user_input["street"])
                if rate >= 95:
                    similar_address += self.data_by_street[street_norm]
            
            return similar_address
        
        if user_input["postcode"] is not None:
            similar_address = []
            for postcode in self.data_by_postcode:
                if postcode.strip() == user_input["postcode"].strip():
                    similar_address += self.data_by_postcode[postcode]

            return similar_address

        return []



if __name__ == "__main__":
    n = Normalizer(contractions_path="../resources/contractions.json")
    a = Finder(data_path="../resources/finder_dump_with_city.csv", normalizer=n)
    similar = a.get_most_similar({"street": "мичуринский проспект",
                                 "housenumber": n.parse_address_suffix("27Б"),
                                  "postcode": None,
                                  "city": None})
    print(similar)
