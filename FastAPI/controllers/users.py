from fastapi import FastAPI
from entities import user


#inicia el server con : uvicorn users:app --reload

app = FastAPI()

@app.get("/users")
async def users():
    return User()