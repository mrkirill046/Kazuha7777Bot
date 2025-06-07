import logging

from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils import constants, get_hostname, get_kernel, get_package_count, get_update_count, get_uptime
from utils import get_os_name

router = Router()


@router.callback_query(F.data == "status")
async def status_query(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()

    builder.row(
        types.InlineKeyboardButton(text=constants.back_command, callback_data="back_to_commands")
    )

    await callback.answer(text=constants.wait_message)

    computer_status = (
        f"🖥 Имя ПК: `{get_hostname()}`\n"
        f"⚙️ ОС: `{get_os_name()}`\n"
        f"📦 Ядро: `{get_kernel()}`\n"
        f"📈 Аптайм: `{get_uptime()}`\n"
        f"📦 Пакетов: `{get_package_count()}`\n"
        f"⬆️ Обновлений: `{get_update_count()}`\n"
    )

    logging.info("Computer status: %s", computer_status)

    if callback.message is not None:
        await callback.message.edit_text(
            text=computer_status,
            parse_mode="Markdown",
            reply_markup=builder.as_markup()
        )
    else:
        await callback.answer(
            text=constants.error_message
        )


@router.message(Command("status"))
async def status_command(message: types.Message):
    msg = await message.reply(text=constants.wait_message)

    computer_status = (
        f"🖥 Имя ПК: `{get_hostname()}`\n"
        f"⚙️ ОС: `{get_os_name()}`\n"
        f"📦 Ядро: `{get_kernel()}`\n"
        f"📈 Аптайм: `{get_uptime()}`\n"
        f"📦 Пакетов: `{get_package_count()}`\n"
        f"⬆️ Обновлений: `{get_update_count() if get_update_count() != "0" else "нет"}`\n"
    )

    logging.info("Computer status: %s", computer_status)

    try:
        await msg.edit_text(
            text=computer_status,
            parse_mode="Markdown"
        )
    except Exception:
        await msg.edit_text(
            text=constants.error_message
        )
