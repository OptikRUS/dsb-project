import asyncio
import logging
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from config.settings import bot_settings


bot = Bot(token=bot_settings.bot_token)
dp = Dispatcher()


@dp.message()
async def answer_message(message: types.Message):
    await message.answer(text="Hello, world!")


async def main():
    logging.basicConfig(level=logging.DEBUG)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())




