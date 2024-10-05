from pydantic import BaseModel
from typing import List
from pyobjectID import MongoObjectId, PyObjectId
from models.countries import Country


class Coordinates(BaseModel):
    latitude: float
    longitude: float


class GetCity(BaseModel):
    name: str
    population: int
    area_km2: float
    coordinates: Coordinates
    famous_landmarks: List[str]
    country_id: MongoObjectId


class GetCityWithCountry(BaseModel):
    name: str
    population: int
    area_km2: float
    coordinates: Coordinates
    famous_landmarks: List[str]
    country: Country


class PushCity(BaseModel):
    name: str
    population: int
    area_km2: float
    coordinates: Coordinates
    famous_landmarks: List[str]
    country_id: PyObjectId
