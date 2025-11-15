import osmium
import pandas as pd

from normalizer import Normalizer


class Handler(osmium.SimpleHandler):
    def __init__(self):
        super().__init__()
        self.access_keys = {"addr:street", "addr:postcode", "addr:housenumber"}
        self.normalizer = Normalizer()
        self.rows = []

    def relation(self, r):
        # интересуют только здания
        if "building" not in r.tags:
            return
        if "addr:city" not in r.tags:
            return
        if r.tags["addr:city"] != "Москва":
            return

        rel_id = r.id

        for key, value in r.tags:
            # если тег начинается с addr:
            if key.startswith("addr:") and key in self.access_keys:
                if key == "addr:street":
                    self.rows.append({
                        # "id": rel_id,
                        "addr": key,
                        "value": self.normalizer.normalize_sentence(value)
                    })
                else:
                    self.rows.append({
                        # "id": rel_id,
                        "addr": key,
                        "value": value
                    })


# читаем файл
h = Handler()
h.apply_file("central-fed-district-251113.osm.pbf", locations=True)

# собираем датафрейм
df = pd.DataFrame(h.rows, columns=["addr", "value"])

# df = df.drop_duplicates()
df = df.groupby(["addr", "value"]).size().reset_index(name="count")

print(df.head())
print("Всего строк:", len(df))

# сохраняем
df.to_csv("buildings_addr_list_normalized.csv", index=False, encoding="utf-8")
