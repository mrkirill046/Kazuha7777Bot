from abc import ABC
from aiogram import Router, types
from aiogram.filters import Filter
from utils import constants, create_menu, config

router = Router()

class CommandNotInListFilter(Filter, ABC):
    def __init__(self):
        self.allowed_commands = {
            command["slash_command"].lower() for command in config["allowed_commands"]
        }
        self.allowed_commands.add("start")

    async def __call__(self, message: types.Message) -> bool:
        if not message.text or not message.text.startswith("/"):
            return False

        command = message.text[1:].split()[0].lower()

        return command not in self.allowed_commands

@router.message(CommandNotInListFilter())
async def unknown_command(message: types.Message):
    builder = create_menu()

    await message.reply(
        text=constants.not_found_message,
        reply_markup=builder.as_markup(resize_keyboard=True)
    )
