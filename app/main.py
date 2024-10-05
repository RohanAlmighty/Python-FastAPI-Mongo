from fastapi import FastAPI
import uvicorn
from routes.city_router import router as city_router
from routes.country_router import router as country_router

app = FastAPI()

app.include_router(city_router, prefix="/cities")
app.include_router(country_router, prefix="/countries")

if __name__ == "__main__":
    uvicorn.run(app, port=8005, host="0.0.0.0")
