from sqlalchemy.orm import Session
from src.utils import models
from src.utils.db import SessionLocal
from src.category.services import create_food_category
from src.item.services import create_food_item
from src.category.schemas import CategoryCreate
from src.item.schemas import ItemCreate
import asyncio

import json

db = SessionLocal()


async def add_category_and_items():
    with open("/app/fake_data/fake.json", "r") as file:
        parsed_data = json.load(file)

    for category in parsed_data["categories"]:
        created_category = await create_food_category(
            db, category_in=CategoryCreate(**{"name": category["category"]})
        )

        for item in category["items"]:
            await create_food_item(
                db,
                item_in=ItemCreate(
                    **{
                        "name": item["name"],
                        "price": item["price"],
                        "description": item["description"],
                        "category_id": created_category.id,
                    }
                ),
            )


asyncio.run(add_category_and_items())
