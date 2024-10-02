from pydantic import BaseModel, Field
from typing import List


class Coordinates(BaseModel):
    latitude: float
    longitude: float


class City(BaseModel):
    name: str
    country: str
    population: int
    area_km2: float
    coordinates: Coordinates
    famous_landmarks: List[str]
