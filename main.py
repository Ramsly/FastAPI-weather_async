import asyncio

from fastapi import FastAPI

from services import get_weather

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "This is Weather app in FastAPI"}


@app.get("/{city}")
async def city(city: str):
    results = await asyncio.gather(asyncio.create_task(get_weather(city)))
    return results
