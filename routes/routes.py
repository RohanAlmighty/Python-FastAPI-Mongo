from fastapi import APIRouter
from models.cities import City
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


@router.get("/")
async def get_cities():
    cities = list_serial(collection_name.find())
    return cities


@router.post("/")
async def post_city(city: City):
    collection_name.insert_one(city.model_dump())


@router.put("/")
async def put_city(id: str, city: City):
    collection_name.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": city.model_dump()}
    )


@router.delete("/")
async def delete_city(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
