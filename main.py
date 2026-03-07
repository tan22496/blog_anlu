from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def hw():
    return "Hello World"

# run : uvicorn main:app --reload