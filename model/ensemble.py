from typing import List, Dict

import pandas as pd

from model.main import Validator
from model.new_ner import NERTrainer


class Ensamble:
    def __init__(self, validator: Validator):
        self.validator = validator
        self.ner_extractor = NERTrainer.load_from_path("/app/model_data")

    def process_text(self, text: str) -> dict:
        topos: list[dict] = self.ner_extractor.predict([text])
        for topo in topos:
            validation_verdict = self.validator.predict(topo["text"])
            print(validation_verdict)



if __name__ == '__main__':
    e = Ensamble(
        validator=Validator(init_df_osm=pd.read_csv("model/data/test.csv"))
    )
    print(e.process_text("119361 больший очаковский улица 47А"))