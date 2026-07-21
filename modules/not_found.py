from aiogram import Router, types
from aiogram.filters import Filter

from utils import constants, create_menu, registered_commands

router = Router()


class CommandNotInListFilter(Filter):
    async def __call__(self, message: types.Message) -> bool:
        if not message.text or not message.text.startswith("/"):
            return False

        command = message.text[1:].split()[0].lower()

        allowed = {cmd["callback_data"].lower() for cmd in registered_commands}
        allowed.add("start")

        return command not in allowed


@router.message(CommandNotInListFilter())
async def unknown_command(message: types.Message) -> None:
    builder = create_menu()

    await message.reply(
        text=constants.not_found_message,
        reply_markup=builder.as_markup(resize_keyboard=True),
    )
