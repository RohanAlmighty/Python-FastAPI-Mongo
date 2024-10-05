from fastapi import APIRouter, HTTPException
from models.countries import Country
from config.database import countries_collection_name as collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


@router.get("/")
async def get_countries():
    try:
        countries = list_serial(list(collection_name.find()), Country)
        return countries
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="error fetching countries: " + str(e)
        )


@router.post("/")
async def post_country(country: Country):
    try:
        collection_name.insert_one(country.model_dump())
        return {"message": "country added successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="error adding country: " + str(e)
        )


@router.put("/")
async def put_country(id: str, country: Country):
    try:
        result = collection_name.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": country.model_dump()}
        )
        if result:
            return {"message": "country updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="country not found")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="error updating country: " + str(e)
        )


@router.delete("/")
async def delete_country(id: str):
    try:
        result = collection_name.find_one_and_delete({"_id": ObjectId(id)})
        if result:
            return {"message": "country deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="country not found")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="error deleting country: " + str(e)
        )
