from fastapi import FastAPI
from fastapi.params import Body
from app.auth.view import router as auth_router
app = FastAPI()


app.include_router(auth_router)

@app.get("/")
async def root(data):
    return {"message": "Hello World"}
