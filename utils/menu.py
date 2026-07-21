from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from utils import constants


def create_menu() -> ReplyKeyboardBuilder:
    keyboard = ReplyKeyboardBuilder()

    keyboard.row(
        types.KeyboardButton(text=constants.user_button),
        types.KeyboardButton(text=constants.command_button),
    )

    return keyboard
