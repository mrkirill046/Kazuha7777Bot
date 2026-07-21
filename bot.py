import asyncio
import logging
import os
import signal

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from utils import constants, load_all_modules, registered_commands

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(
            os.path.join("logs", constants.log_filename), encoding="utf-8"
        ),
        logging.StreamHandler(),
    ],
)

bot = Bot(constants.token, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

registered_commands.extend(load_all_modules(dp))


async def main() -> None:
    loop = asyncio.get_running_loop()

    for sig in (signal.SIGTERM, signal.SIGINT):
        loop.add_signal_handler(sig, lambda: asyncio.create_task(dp.stop_polling()))

    logging.info("Bot started")

    await dp.start_polling(bot)

    logging.info("Bot stopped")


if __name__ == "__main__":
    asyncio.run(main())
