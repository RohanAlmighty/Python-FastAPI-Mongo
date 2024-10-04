from fastapi import APIRouter, HTTPException
from models.cities import City
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


@router.get("/")
async def get_cities():
    try:
        cities = list_serial(collection_name.find())
        return cities
    except:
        raise HTTPException(status_code=500, detail="error fetching cities")


@router.post("/")
async def post_city(city: City):
    try:
        collection_name.insert_one(city.model_dump())
        return {"message": "city added successfully"}
    except:
        raise HTTPException(status_code=500, detail="error adding city")


@router.put("/")
async def put_city(id: str, city: City):
    try:
        result = collection_name.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": city.model_dump()}
        )
        if result:
            return {"message": "city updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="city not found")
    except HTTPException as e:
        raise e
    except:
        raise HTTPException(status_code=500, detail="error updating city")


@router.delete("/")
async def delete_city(id: str):
    try:
        result = collection_name.find_one_and_delete({"_id": ObjectId(id)})
        if result:
            return {"message": "city deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="city not found")
    except HTTPException as e:
        raise e
    except:
        raise HTTPException(status_code=500, detail="error deleting city")
