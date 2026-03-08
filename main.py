from fastapi import FastAPI

from database import models
from database.database import engine


app = FastAPI()

@app.get("/")
def hw():
    return "Hello World"

models.Base.metadata.create_all(engine)

# run : uvicorn main:app --reload