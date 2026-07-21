import asyncio

from aiogram import F, Router, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils import OwnerOnlyMiddleware, constants, reboot

router = Router()

COMMAND_META = {
    "name": "Restart",
    "description": "Restart the computer",
    "callback_data": "restart",
}

router.callback_query.middleware(OwnerOnlyMiddleware())
router.message.middleware(OwnerOnlyMiddleware())


@router.callback_query(F.data == "restart")
async def restart_query(callback: types.CallbackQuery) -> None:
    builder = InlineKeyboardBuilder()

    builder.row(
        types.InlineKeyboardButton(
            text=constants.no_restart_command, callback_data="no_restart"
        ),
        types.InlineKeyboardButton(
            text=constants.yes_restart_command, callback_data="yes_restart"
        ),
    )

    await callback.message.edit_text(
        text=constants.restart_message, reply_markup=builder.as_markup()
    )


@router.message(Command("restart"))
async def restart_command(message: types.Message) -> None:
    builder = InlineKeyboardBuilder()

    builder.row(
        types.InlineKeyboardButton(
            text=constants.no_restart_command, callback_data="no_restart"
        ),
        types.InlineKeyboardButton(
            text=constants.yes_restart_command, callback_data="yes_restart"
        ),
    )

    await message.reply(
        text=constants.restart_message, reply_markup=builder.as_markup()
    )


@router.callback_query(F.data == "yes_restart")
async def yes_restart_query(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(text="Restarting...")
    await asyncio.sleep(1)

    reboot()


@router.callback_query(F.data == "no_restart")
async def no_restart_query(callback: types.CallbackQuery) -> None:
    builder = InlineKeyboardBuilder()

    builder.row(
        types.InlineKeyboardButton(
            text=constants.back_command, callback_data="back_to_commands"
        )
    )

    await callback.message.edit_text(
        text="Restart cancelled!", reply_markup=builder.as_markup()
    )
