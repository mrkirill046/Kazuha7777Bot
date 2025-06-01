import asyncio

from aiogram import Router, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.command import Command
from utils import constants, config, shutdown

router = Router()

@router.callback_query(F.data == "shutdown")
async def shutdown_query(callback: types.CallbackQuery):
    if callback.from_user.id == config["owner_id"]:
        builder = InlineKeyboardBuilder()

        builder.row(
            types.InlineKeyboardButton(text=constants.no_shutdown_command, callback_data="no_shutdown"),
            types.InlineKeyboardButton(text=constants.yes_shutdown_command, callback_data="yes_shutdown")
        )

        await callback.message.edit_text(
            text=constants.shutdown_message,
            reply_markup=builder.as_markup()
        )
    else:
        await callback.answer(text=constants.not_allowed_message)

@router.message(Command("shutdown"))
async def shutdown_command(message: types.Message):
    if message.from_user.id == config["owner_id"]:
        builder = InlineKeyboardBuilder()

        builder.row(
            types.InlineKeyboardButton(text=constants.no_shutdown_command, callback_data="no_shutdown"),
            types.InlineKeyboardButton(text=constants.yes_shutdown_command, callback_data="yes_shutdown")
        )

        await message.reply(
            text=constants.shutdown_message,
            reply_markup=builder.as_markup()
        )
    else:
        await message.reply(text=constants.not_allowed_message)

@router.callback_query(F.data == "yes_shutdown")
async def yes_shutdown_query(callback: types.CallbackQuery):
    if callback.from_user.id == config["owner_id"]:
        await callback.message.edit_text(text="Выключаюсь...")
        await asyncio.sleep(1)

        shutdown()
    else:
        await callback.answer(text=constants.not_allowed_message)

@router.callback_query(F.data == "no_shutdown")
async def no_shutdown_query(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()

    builder.row(
        types.InlineKeyboardButton(text=constants.back_command, callback_data="back_to_commands")
    )

    if callback.from_user.id == config["owner_id"]:
        await callback.message.edit_text(
            text="Перезагрузка отменена!",
            reply_markup=builder.as_markup()
        )
    else:
        await callback.answer(text=constants.not_allowed_message)
