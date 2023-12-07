import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart, Command
from tortoise import Tortoise


from config.settings import bot_settings
from config.db import init, create_user

bot = Bot(token=bot_settings.bot_token)
dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text="Hello, world!")


@dp.message(Command("create_user"))
async def cmd_create_user(message: types.Message):
    user = await create_user("example_user")
    await message.answer(f"User created: {user.name}")


async def main():
    logging.basicConfig(level=logging.DEBUG)
    await init()
    await dp.start_polling(bot)
    await Tortoise.close_connections()

if __name__ == "__main__":
    asyncio.run(main())
