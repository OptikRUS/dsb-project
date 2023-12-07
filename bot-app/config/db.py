from tortoise import Tortoise

from models.users import Client
from config.settings import settings


async def init():
    await Tortoise.init(
        db_url=settings.DATABASE.default,
        modules={
            "models": [
                "models.users",
                "models.tickets",
                "models.services",
                "models.bot",
            ]
        },
    )
    await Tortoise.generate_schemas()


async def create_user(name: str):
    user = await Client.create(name=name)
    return user
