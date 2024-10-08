from fastapi import FastAPI
from enum import Enum

food_items = {
    "indian": ["samosa", "chole"],
    "italian": ["pizza", "pasta"],
    "chinese": ["noodles", "fried rice"]
}

class AvailableCuisines(str, Enum):
    indian = "indian"
    italian = "italian"
    chinese = "chinese"

app = FastAPI()

@app.get("/hello")
async def hello():
    return {"Hello World"}

@app.get("/get_items/{cuisine}")
async def get_items(cuisine: AvailableCuisines):
    return food_items.get(cuisine)
