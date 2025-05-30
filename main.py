import asyncio
import logging

from modules import *
from utils import constants, load_all_modules
from aiogram import Bot, Dispatcher

logging.basicConfig(level=logging.INFO)

bot = Bot(constants.token)
dp = Dispatcher()

load_all_modules(dp)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
