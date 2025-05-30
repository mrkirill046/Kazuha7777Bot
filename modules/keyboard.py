from aiogram import Router, types, F
from aiogram.filters.command import Command
from utils import constants

router = Router()

@router.message(F.text == constants.settings_button)
async def settings(message: types.Message):
    await message.reply("В разработке!")

@router.message(F.text == constants.user_button)
async def user(message: types.Message):
    await message.reply("В разработке!")

@router.message(F.text == constants.command_button)
async def command(message: types.Message):
    await message.reply("В разработке!")
