from pydantic import BaseModel
from typing import List


class Country(BaseModel):
    name: str
    capital: str
    population: int
    area_km2: float
    continent: str
    currency: str
    languages: List[str]
