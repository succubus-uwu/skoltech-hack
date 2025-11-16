from typing import List, Dict

from model.main import Validator
from model.new_ner import NERTrainer


class Ensamble:
    def __init__(self, validator: Validator):
        self.validator = validator
        self.ner_extractor = NERTrainer.load_from_path("/app/model")

    def process_text(self, text: str) -> dict:
        topos: list[dict] = self.ner_extractor.predict([text])
        for topo in topos:
            validation_verdict = self.validator.predict(topo["text"])
            print(validation_verdict)



