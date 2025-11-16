from typing import Optional

from pydantic import BaseModel


class ObjectLocation(BaseModel):
    locality: Optional[str]
    street: Optional[str]
    number: Optional[str]
    lon: float
    lat: float

class ResponseSchema(BaseModel):
    searched_address: Optional[str]
    objects: list[ObjectLocation]
