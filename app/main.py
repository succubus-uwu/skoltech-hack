from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.finder import Finder
from app.normalizer import Normalizer
from app.schemas import ResponseSchema, ObjectLocation


@asynccontextmanager
async def lifespan(app: FastAPI):
    global FINDER
    n = Normalizer(contractions_path="./resources/contractions.json")
    FINDER = Finder(data_path="./resources/finder_dump_with_city.csv", normalizer=n)
    yield


app = FastAPI(lifespan=lifespan)

@app.get("/")
async def hello():
    return {"hello"}

@app.get("/send_request")
async def send_request(input: str) -> ResponseSchema:
    # TODO Код парсера
    user_input = {"street": "мичуринский проспект",
                  "housenumber": "27Б к2",
                  "city": None,
                  "postcode": None}
    user_input["housenumber"] = FINDER.normalizer.parse_address_suffix(user_input["housenumber"])
    similars = FINDER.get_most_similar(user_input)
    objects = []
    for similar in similars:
        print(similar)
        coord = FINDER.centroid_mean(coords=similar[4])
        object = ObjectLocation(locality=similar[3],
                                street=similar[0],
                                number=similar[1],
                                lon=coord[1],
                                lat=coord[0])
        objects.append(object)
    return ResponseSchema(searched_address=input,
                          objects=objects)

# class Handler(osmium.SimpleHandler):
#     def __init__(self):
#         super().__init__()
#         self.access_keys = {"addr:street", "addr:postcode", "addr:housenumber"}
#         self.normalizer = Normalizer()
#         self.rows = []
#
#     def _process_object(self, obj):
#         # интересуют только здания
#         if "building" not in obj.tags:
#             return
#         # только с городом
#         if "addr:city" not in obj.tags:
#             return
#         if obj.tags["addr:city"] != "Москва":
#             return
#
#         obj_id = obj.id  # если захочешь использовать id, будет под рукой
#
#         # перебираем теги
#         for key, value in obj.tags:
#             # если тег начинается с addr: и входит в список нужных ключей
#             if key.startswith("addr:") and key in self.access_keys:
#                 if key == "addr:street":
#                     self.rows.append({
#                         # "id": obj_id,
#                         "addr": key,
#                         "value": self.normalizer.normalize_sentence(value)
#                     })
#                 else:
#                     self.rows.append({
#                         # "id": obj_id,
#                         "addr": key,
#                         "value": value
#                     })
#
#     def relation(self, r):
#         # здания, оформленные как relation (мультиполигоны)
#         self._process_object(r)
#
#     def way(self, w):
#         # здания, оформленные как way (самый частый случай)
#         self._process_object(w)
#
#
# # читаем файл
# h = Handler()
# h.apply_file("central-fed-district-251113.osm.pbf", locations=True)
#
# # собираем датафрейм
# df = pd.DataFrame(h.rows, columns=["addr", "value"])
#
# # группируем и считаем количество вхождений
# df = df.groupby(["addr", "value"]).size().reset_index(name="count")
#
# print(df.head())
# print("Всего строк:", len(df))
#
# # сохраняем
# df.to_csv("buildings_addr_list_normalized.csv", index=False, encoding="utf-8")
