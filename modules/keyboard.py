from aiogram import Router, types, F
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from utils import constants, config

router = Router()

@router.message(F.text == constants.settings_button)
async def settings(message: types.Message):
    builder = ReplyKeyboardBuilder()
    
    builder.row(
        types.KeyboardButton(text=constants.back_command)
    )
    
    await message.reply(
        text=constants.settings_message,
        reply_markup=builder.as_markup(resize_keyboard=True)
    )

@router.message(F.text == constants.user_button)
async def user(message: types.Message):
    user = message.from_user
    
    builder = ReplyKeyboardBuilder()
    
    builder.row(
        types.KeyboardButton(text=constants.back_command)
    )
    
    if user is not None:
        await message.reply(
            text=(
                f"👤 *Личный кабинет*\n\n"
                f"📛 Имя: {user.full_name}\n"
                f"🆔 Telegram ID: `{user.id}`\n"
                f"💼 Статус: {"Полный доступ" if user.id == config["owner_id"] else "Ограниченный доступ"}\n"
            ),
            parse_mode="Markdown",
            reply_markup=builder.as_markup(resize_keyboard=True)
        )
    else:
        await message.reply(text=constants.error_message)

@router.message(F.text == constants.command_button)
async def command(message: types.Message):
    builder = InlineKeyboardBuilder()
    
    if any(config["allowed_commands"]):
        for command in config["allowed_commands"]:
            builder.row(
                types.InlineKeyboardButton(text=command["name"], callback_data=command["slash_command"])
            )
            
    await message.reply(
        text=constants.command_message,
        reply_markup=builder.as_markup()
    )
