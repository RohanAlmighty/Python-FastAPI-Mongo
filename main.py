from fastapi import FastAPI
import uvicorn
from routes.routes import router

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, port=8005, host="0.0.0.0")
