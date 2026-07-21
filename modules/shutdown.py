import asyncio

from aiogram import F, Router, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils import OwnerOnlyMiddleware, constants, shutdown

router = Router()

COMMAND_META = {
    "name": "Shutdown",
    "description": "Shut down the computer",
    "callback_data": "shutdown",
}

router.callback_query.middleware(OwnerOnlyMiddleware())
router.message.middleware(OwnerOnlyMiddleware())


@router.callback_query(F.data == "shutdown")
async def shutdown_query(callback: types.CallbackQuery) -> None:
    builder = InlineKeyboardBuilder()

    builder.row(
        types.InlineKeyboardButton(
            text=constants.no_shutdown_command, callback_data="no_shutdown"
        ),
        types.InlineKeyboardButton(
            text=constants.yes_shutdown_command, callback_data="yes_shutdown"
        ),
    )

    await callback.message.edit_text(
        text=constants.shutdown_message, reply_markup=builder.as_markup()
    )


@router.message(Command("shutdown"))
async def shutdown_command(message: types.Message) -> None:
    builder = InlineKeyboardBuilder()

    builder.row(
        types.InlineKeyboardButton(
            text=constants.no_shutdown_command, callback_data="no_shutdown"
        ),
        types.InlineKeyboardButton(
            text=constants.yes_shutdown_command, callback_data="yes_shutdown"
        ),
    )

    await message.reply(
        text=constants.shutdown_message, reply_markup=builder.as_markup()
    )


@router.callback_query(F.data == "yes_shutdown")
async def yes_shutdown_query(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(text="Shutting down...")
    await asyncio.sleep(1)

    shutdown()


@router.callback_query(F.data == "no_shutdown")
async def no_shutdown_query(callback: types.CallbackQuery) -> None:
    builder = InlineKeyboardBuilder()

    builder.row(
        types.InlineKeyboardButton(
            text=constants.back_command, callback_data="back_to_commands"
        )
    )

    await callback.message.edit_text(
        text="Shutdown cancelled!", reply_markup=builder.as_markup()
    )
