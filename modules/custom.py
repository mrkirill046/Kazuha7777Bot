import shlex
import subprocess

from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils import CustomCommand, OwnerOnlyMiddleware, constants

router = Router()

COMMAND_META = {
    "name": "Custom Command",
    "description": "Run a custom terminal command",
    "callback_data": "custom",
}

router.callback_query.middleware(OwnerOnlyMiddleware())
router.message.middleware(OwnerOnlyMiddleware())


@router.callback_query(F.data == "custom")
async def enter_custom_command_query(
    callback: types.CallbackQuery, state: FSMContext
) -> None:
    await callback.message.edit_text(text=constants.enter_command_message)
    await state.set_state(CustomCommand.waiting_for_command_alt)


@router.message(Command("custom"))
async def enter_custom_command(message: types.Message, state: FSMContext) -> None:
    await message.reply(text=constants.enter_command_message)
    await state.set_state(CustomCommand.waiting_for_command)


async def run_command_and_prepare_response(
    command: str, with_back_button: bool = False
) -> tuple[str, InlineKeyboardBuilder | None]:
    builder = None

    if with_back_button:
        builder = InlineKeyboardBuilder()

        builder.row(
            types.InlineKeyboardButton(
                text=constants.back_command, callback_data="back_to_commands"
            )
        )

    try:
        result = subprocess.run(
            shlex.split(command),
            capture_output=True,
            text=True,
            timeout=30,
        )

        output = result.stdout or "(empty output)"
        error = result.stderr

        response = f"Command executed:\n\n<code>{command}</code>\n\nOutput:\n<pre>{output}</pre>"

        if error:
            response += f"\nErrors:\n<pre>{error}</pre>"

    except subprocess.TimeoutExpired:
        response = "Command timed out and was aborted."
    except FileNotFoundError:
        response = f"Command not found: <code>{command.split()[0]}</code>"
    except Exception as e:
        response = f"Error while executing:\n<pre>{e}</pre>"

    return response, builder


@router.message(CustomCommand.waiting_for_command)
async def execute_custom_command(message: types.Message, state: FSMContext) -> None:
    if not message.text:
        await state.clear()

        return

    response, _ = await run_command_and_prepare_response(message.text)

    await message.reply(response, parse_mode="HTML")
    await state.clear()


@router.message(CustomCommand.waiting_for_command_alt)
async def execute_custom_command_query(
    message: types.Message, state: FSMContext
) -> None:
    if not message.text:
        await state.clear()

        return

    response, builder = await run_command_and_prepare_response(
        message.text, with_back_button=True
    )

    await message.reply(
        response,
        parse_mode="HTML",
        reply_markup=builder.as_markup(resize_keyboard=True) if builder else None,
    )

    await state.clear()
