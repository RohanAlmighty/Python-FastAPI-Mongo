from fastapi import APIRouter, HTTPException
from models.cities import GetCity, GetCityWithCountry, PushCity
from config.database import db, cities_collection_name as collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


@router.get("/")
async def get_cities():
    try:
        cities = list_serial(list(collection_name.find()), GetCity)
        return cities
    except:
        raise HTTPException(status_code=500, detail="error fetching cities")


@router.get("/cities_with_country")
async def get_cities_with_country():
    try:
        pipeline = [
            {
                "$lookup": {
                    "from": "countries",
                    "localField": "country_id",
                    "foreignField": "_id",
                    "as": "country_data",
                }
            },
            {"$unwind": "$country_data"},
            {
                "$project": {
                    "name": 1,
                    "population": 1,
                    "area_km2": 1,
                    "coordinates": 1,
                    "famous_landmarks": 1,
                    "country": "$country_data",
                }
            },
        ]
        cities = list_serial(
            list(db["cities"].aggregate(pipeline)), GetCityWithCountry
        )
        return cities
    except:
        raise HTTPException(
            status_code=500, detail="error fetching cities with country"
        )


@router.post("/")
async def post_city(city: PushCity):
    try:
        collection_name.insert_one(city.model_dump())
        return {"message": "city added successfully"}
    except:
        raise HTTPException(status_code=500, detail="error adding city")


@router.put("/")
async def put_city(id: str, city: PushCity):
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
