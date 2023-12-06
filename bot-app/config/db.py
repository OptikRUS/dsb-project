from tortoise import Tortoise

from models.models_users import Client
from config.settings import database_url


async def init():
    await Tortoise.init(
        db_url=database_url,
        modules={
            "models": [
                "models.models_users",
                "models.models_tickets",
                "models.models_services",
                "models.models_bot",
            ]
        },
    )
    print()
    await Tortoise.generate_schemas()
    print()


async def create_user(name: str):
    user = await Client.create(name=name)
    return user
