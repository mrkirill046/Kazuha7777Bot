from aiogram import Router, types
from aiogram.filters.command import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils import constants, create_menu

router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message) -> None:
    inline = InlineKeyboardBuilder()

    inline.row(
        types.InlineKeyboardButton(
            text=constants.tgc_button, url="https://t.me/Kazuha_IT"
        )
    )

    keyboard = create_menu()

    user_name = message.from_user.first_name if message.from_user else None

    await message.answer(
        text=f"Hello, {user_name}!" if user_name else "Hello!",
        reply_markup=keyboard.as_markup(resize_keyboard=True),
    )

    await message.answer(
        text=constants.welcome_message, reply_markup=inline.as_markup()
    )
