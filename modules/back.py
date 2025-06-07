from aiogram import Router, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils import constants, create_menu, config

router = Router()


@router.message(F.text == constants.back_command)
async def settings(message: types.Message):
    keyboard = create_menu()

    await message.reply(
        text="Понял тебя, возвращаемся назад!",
        reply_markup=keyboard.as_markup(resize_keyboard=True)
    )


@router.callback_query(F.data == "back_to_commands")
async def back_to_commands(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()

    if any(config["allowed_commands"]):
        for command in config["allowed_commands"]:
            builder.row(
                types.InlineKeyboardButton(text=command["name"], callback_data=command["slash_command"])
            )

    await callback.message.edit_text(
        text="Понял тебя, возвращаемся назад!",
        reply_markup=None
    )

    await callback.message.reply(
        text=constants.command_message,
        reply_markup=builder.as_markup()
    )


@router.callback_query(F.data == "back_to_commands_alt")
async def back_to_commands(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()

    if any(config["allowed_commands"]):
        for command in config["allowed_commands"]:
            builder.row(
                types.InlineKeyboardButton(text=command["name"], callback_data=command["slash_command"])
            )

    await callback.message.edit_caption(
        reply_markup=None,
        caption="Понял тебя, возвращаемся назад!"
    )

    await callback.message.reply(
        text=constants.command_message,
        reply_markup=builder.as_markup()
    )
