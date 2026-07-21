from aiogram import F, Router, types
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from utils import config, constants, registered_commands

router = Router()


@router.message(F.text == constants.user_button)
async def user(message: types.Message) -> None:
    user = message.from_user

    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text=constants.back_command))

    if user is not None:
        status = "Full access" if user.id == config["owner_id"] else "Restricted access"

        await message.reply(
            text=(
                f"Profile\n\n"
                f"Name: {user.full_name}\n"
                f"Telegram ID: `{user.id}`\n"
                f"Status: {status}\n"
            ),
            parse_mode="Markdown",
            reply_markup=builder.as_markup(resize_keyboard=True),
        )
    else:
        await message.reply(text=constants.error_message)


@router.message(F.text == constants.command_button)
async def command(message: types.Message) -> None:
    builder = InlineKeyboardBuilder()

    for cmd in registered_commands:
        builder.row(
            types.InlineKeyboardButton(
                text=cmd["name"], callback_data=cmd["callback_data"]
            )
        )

    await message.reply(
        text=constants.command_message, reply_markup=builder.as_markup()
    )
