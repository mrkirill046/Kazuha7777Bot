import logging

from aiogram import F, Router, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils import (
    constants,
    get_hostname,
    get_kernel,
    get_os_name,
    get_system_packages,
    get_uptime,
)

router = Router()

COMMAND_META = {
    "name": "Status",
    "description": "Check computer status",
    "callback_data": "status",
}


def _build_status_text() -> str:
    sys_pkgs = get_system_packages()

    return (
        f"🖥 Host: <code>{get_hostname()}</code>\n"
        f"🐧 OS: <code>{get_os_name()}</code>\n"
        f"⚙️ Kernel: <code>{get_kernel()}</code>\n"
        f"🕐 Uptime: <code>{get_uptime()}</code>\n"
        f"📦 Packages: <code>{sys_pkgs}</code> (system)\n"
    )


@router.callback_query(F.data == "status")
async def status_query(callback: types.CallbackQuery) -> None:
    builder = InlineKeyboardBuilder()

    builder.row(
        types.InlineKeyboardButton(
            text=constants.back_command, callback_data="back_to_commands"
        )
    )

    await callback.answer(text=constants.wait_message)

    computer_status = _build_status_text()
    logging.info("Computer status: %s", computer_status)

    if callback.message is not None:
        await callback.message.edit_text(
            text=computer_status, parse_mode="HTML", reply_markup=builder.as_markup()
        )
    else:
        await callback.answer(text=constants.error_message)


@router.message(Command("status"))
async def status_command(message: types.Message) -> None:
    msg = await message.reply(text=constants.wait_message)

    computer_status = _build_status_text()
    logging.info("Computer status: %s", computer_status)

    try:
        await msg.edit_text(text=computer_status, parse_mode="HTML")
    except Exception:
        await msg.edit_text(text=constants.error_message)
