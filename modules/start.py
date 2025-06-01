from aiogram import Router, types
from aiogram.filters.command import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils import constants, create_menu

router = Router()

@router.message(CommandStart())
async def start_handler(message: types.Message):
    inline = InlineKeyboardBuilder()
    
    inline.row(
        types.InlineKeyboardButton(text=constants.tgc_button, url="https://t.me/Kazuha_IT")
    )
    
    keyboard = create_menu()
    
    if message.from_user is not None:
        await message.answer(
            text=f"Привет, {message.from_user.first_name}!",
            reply_markup=keyboard.as_markup(resize_keyboard=True)
        )
    else:
        await message.answer(
            text="Привет!",
            reply_markup=keyboard.as_markup(resize_keyboard=True)
        )

    await message.answer(
        text=constants.welcome_message,
        reply_markup=inline.as_markup()
    )
