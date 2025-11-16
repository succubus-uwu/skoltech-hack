from model.main import Validator
from model.new_ner import NERTrainer


class Ensamble:
    def __init__(self, validator: Validator):
        self.validator = validator
        self.ner_extractor = NERTrainer.load_from_path("/app/model")

    def process_text(self, text: str) -> dict:
        self.ner_extractor.predict([text])

