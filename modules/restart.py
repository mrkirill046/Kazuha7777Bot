import asyncio

from aiogram import Router, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.command import Command
from utils import constants, config, reboot

router = Router()


@router.callback_query(F.data == "restart")
async def restart_query(callback: types.CallbackQuery):
    if callback.from_user.id == config["owner_id"]:
        builder = InlineKeyboardBuilder()

        builder.row(
            types.InlineKeyboardButton(text=constants.no_restart_command, callback_data="no_restart"),
            types.InlineKeyboardButton(text=constants.yes_restart_command, callback_data="yes_restart")
        )

        await callback.message.edit_text(
            text=constants.restart_message,
            reply_markup=builder.as_markup()
        )
    else:
        await callback.answer(text=constants.not_allowed_message)


@router.message(Command("restart"))
async def restart_command(message: types.Message):
    if message.from_user.id == config["owner_id"]:
        builder = InlineKeyboardBuilder()

        builder.row(
            types.InlineKeyboardButton(text=constants.no_restart_command, callback_data="no_restart"),
            types.InlineKeyboardButton(text=constants.yes_restart_command, callback_data="yes_restart")
        )

        await message.reply(
            text=constants.restart_message,
            reply_markup=builder.as_markup()
        )
    else:
        await message.reply(text=constants.not_allowed_message)


@router.callback_query(F.data == "yes_restart")
async def yes_restart_query(callback: types.CallbackQuery):
    if callback.from_user.id == config["owner_id"]:
        await callback.message.edit_text(text="Перезагружаюсь...")
        await asyncio.sleep(1)

        reboot()
    else:
        await callback.answer(text=constants.not_allowed_message)


@router.callback_query(F.data == "no_restart")
async def no_restart_query(callback: types.CallbackQuery):
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
