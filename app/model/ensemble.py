from typing import List, Dict

import pandas as pd

from app.model.main import Validator
from app.model.new_ner import NERTrainer


class Ensamble:
    def __init__(self, validator: Validator):
        self.validator = validator
        self.ner_extractor = NERTrainer.load_from_path("/app/model_data")
        self.labels = {"addr:postcode", "addr:street", "addr:housenumber", "addr:city"}

    def process_text(self, text: str) -> dict:
        topos: dict = self.ner_extractor.predict([text])[0]
        topos_entities: list = topos["entities"]

        result = dict()
        for key in self.labels:
            result[key] = None


        for entity in topos_entities:
            validation_verdict = self.validator.predict(entity[0])
            if entity[1] == validation_verdict[0]:
                result[validation_verdict[0]] = entity[0]

        return result



if __name__ == '__main__':
    e = Ensamble(
        validator=Validator(init_df_osm=pd.read_csv("model/data/test.csv"))
    )
    print(e.process_text("119361 больший очаковский улица 47А"))