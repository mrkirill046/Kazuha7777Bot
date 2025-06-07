import asyncio

from aiogram import Router, types, F, Bot
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.chat_action import ChatActionSender
from aiogram.filters.command import Command
from utils import constants, config, screenshot, delete_screenshot

router = Router()


@router.callback_query(F.data == "screenshot")
async def sent_screenshot_query(callback: types.CallbackQuery, bot: Bot):
    if callback.from_user.id == config["owner_id"]:
        builder = InlineKeyboardBuilder()

        builder.row(
            types.InlineKeyboardButton(text=constants.back_command, callback_data="back_to_commands_alt")
        )

        await callback.message.edit_text(text=constants.wait_message)

        screenshot_path = screenshot()

        async with ChatActionSender.upload_photo(callback.message.chat.id, bot):
            photo_data = screenshot_path.read_bytes()
            input_file = types.BufferedInputFile(photo_data, filename=screenshot_path.name)

            await callback.message.answer_photo(
                caption=f"{callback.from_user.first_name}, вот скриншот вашего компьютера!",
                photo=input_file,
                reply_markup=builder.as_markup()
            )

        await asyncio.sleep(1)

        delete_screenshot(screenshot_path)
    else:
        await callback.answer(text=constants.not_allowed_message)


@router.message(Command("screenshot"))
async def sent_screenshot_command(message: types.Message, bot: Bot):
    if message.from_user.id == config["owner_id"]:
        await message.reply(text=constants.wait_message)

        screenshot_path = screenshot()

        async with ChatActionSender.upload_photo(message.chat.id, bot):
            photo_data = screenshot_path.read_bytes()
            input_file = types.BufferedInputFile(photo_data, filename=screenshot_path.name)

            await message.answer_photo(
                caption=f"{message.from_user.first_name}, вот скриншот вашего компьютера!",
                photo=input_file
            )

        await asyncio.sleep(1)

        delete_screenshot(screenshot_path)
    else:
        await message.answer(text=constants.not_allowed_message)
