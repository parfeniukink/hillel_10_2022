from time import sleep
from random import randint
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    sleep(1)
    return {"random value": randint(1, 100)}
