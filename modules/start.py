from aiogram import Router, types
from aiogram.filters.command import Command

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Hello from modules/start.py!")
