from fastapi import FastAPI
from app.api.routes import router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

app.include_router(router)