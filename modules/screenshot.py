import asyncio
import logging

from aiogram import Bot, F, Router, types
from aiogram.filters.command import Command
from aiogram.utils.chat_action import ChatActionSender
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils import OwnerOnlyMiddleware, constants, delete_screenshot, screenshot

router = Router()

COMMAND_META = {
    "name": "Screenshot",
    "description": "Take a screenshot",
    "callback_data": "screenshot",
}

router.callback_query.middleware(OwnerOnlyMiddleware())
router.message.middleware(OwnerOnlyMiddleware())


@router.callback_query(F.data == "screenshot")
async def sent_screenshot_query(callback: types.CallbackQuery, bot: Bot) -> None:
    builder = InlineKeyboardBuilder()

    builder.row(
        types.InlineKeyboardButton(
            text=constants.back_command, callback_data="back_to_commands_alt"
        )
    )

    await callback.message.edit_text(text=constants.wait_message)

    try:
        screenshot_path = screenshot()
    except Exception as e:
        logging.error("Screenshot failed: %s", e)

        await callback.message.edit_text(
            text=f"Failed to take screenshot:\n<pre>{e}</pre>", parse_mode="HTML"
        )

        return

    async with ChatActionSender.upload_photo(callback.message.chat.id, bot):
        photo_data = screenshot_path.read_bytes()
        input_file = types.BufferedInputFile(photo_data, filename=screenshot_path.name)

        await callback.message.answer_photo(
            caption=f"{callback.from_user.first_name}, here is your screenshot!",
            photo=input_file,
            reply_markup=builder.as_markup(),
        )

    await asyncio.sleep(1)

    delete_screenshot(screenshot_path)


@router.message(Command("screenshot"))
async def sent_screenshot_command(message: types.Message, bot: Bot) -> None:
    msg = await message.reply(text=constants.wait_message)

    try:
        screenshot_path = screenshot()
    except Exception as e:
        logging.error("Screenshot failed: %s", e)

        await msg.edit_text(
            text=f"Failed to take screenshot:\n<pre>{e}</pre>", parse_mode="HTML"
        )

        return

    async with ChatActionSender.upload_photo(message.chat.id, bot):
        photo_data = screenshot_path.read_bytes()
        input_file = types.BufferedInputFile(photo_data, filename=screenshot_path.name)

        await message.answer_photo(
            caption=f"{message.from_user.first_name}, here is your screenshot!",
            photo=input_file,
        )

    await asyncio.sleep(1)

    delete_screenshot(screenshot_path)
