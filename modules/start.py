from aiogram import Router, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from utils import constants

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    inline = InlineKeyboardBuilder()
    
    inline.row(
        types.InlineKeyboardButton(text=constants.tgc_button, url="https://t.me/Kazuha_IT")
    )
    
    keyboard = ReplyKeyboardBuilder()
    
    keyboard.row(
        types.KeyboardButton(text=constants.settings_button),
        types.KeyboardButton(text=constants.user_button)
    )
    
    keyboard.row(
        types.KeyboardButton(text=constants.command_button)
    )
    
    await message.answer(
        text=f"Привет, {message.from_user.first_name}!",
        reply_markup=keyboard.as_markup(resize_keyboard=True)
    )

    await message.answer(
        text=constants.welcome_message,
        reply_markup=inline.as_markup()
    )
