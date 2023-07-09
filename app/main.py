from fastapi import FastAPI
from fastapi.params import Body
app = FastAPI()


@app.post("/")
async def root(data):
    return {"message": "Hello World"}
