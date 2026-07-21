from aiogram import F, Router, types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils import constants, create_menu, registered_commands

router = Router()


def _build_commands_keyboard() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()

    for cmd in registered_commands:
        builder.row(
            types.InlineKeyboardButton(
                text=cmd["name"], callback_data=cmd["callback_data"]
            )
        )

    return builder


@router.message(F.text == constants.back_command)
async def back_handler(message: types.Message) -> None:
    keyboard = create_menu()

    await message.reply(
        text="Going back!",
        reply_markup=keyboard.as_markup(resize_keyboard=True),
    )


@router.callback_query(F.data == "back_to_commands")
async def back_to_commands(callback: types.CallbackQuery) -> None:
    builder = _build_commands_keyboard()

    await callback.message.edit_text(text="Going back!", reply_markup=None)

    await callback.message.reply(
        text=constants.command_message, reply_markup=builder.as_markup()
    )


@router.callback_query(F.data == "back_to_commands_alt")
async def back_to_commands_alt(callback: types.CallbackQuery) -> None:
    builder = _build_commands_keyboard()

    await callback.message.edit_caption(reply_markup=None, caption="Going back!")

    await callback.message.reply(
        text=constants.command_message, reply_markup=builder.as_markup()
    )
