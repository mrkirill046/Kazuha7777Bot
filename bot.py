import asyncio
import os
import logging

from utils import constants, load_all_modules
from aiogram import Bot, Dispatcher

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(os.path.join("logs", constants.log_filename), encoding="utf-8"),
        logging.StreamHandler()
    ]
)

bot = Bot(constants.token)
dp = Dispatcher()

load_all_modules(dp)

async def main():
    os.makedirs("logs", exist_ok=True)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
