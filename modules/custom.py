import subprocess

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils import CustomCommand, constants, config

router = Router()

@router.callback_query(F.data == "custom")
async def enter_custom_command_query(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id == config["owner_id"]:
        await callback.message.edit_text(text=constants.enter_command_message)
        await state.set_state(CustomCommand.waiting_for_command_alt)
    else:
        await callback.answer(text=constants.not_allowed_message)

@router.message(Command("custom"))
async def enter_custom_command(message: types.Message, state: FSMContext):
    if message.from_user.id == config["owner_id"]:
        await message.reply(text=constants.enter_command_message)
        await state.set_state(CustomCommand.waiting_for_command)
    else:
        await message.reply(text=constants.not_allowed_message)

async def run_command_and_prepare_response(command: str, with_back_button: bool = False):
    builder = None

    if with_back_button:
        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(text=constants.back_command, callback_data="back_to_commands"))

    try:
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, timeout=30
        )

        output = result.stdout or "(пустой вывод)"
        error = result.stderr

        response = f"✅ Команда выполнена:\n\n<code>{command}</code>\n\n📤 Вывод:\n<pre>{output}</pre>"

        if error:
            response += f"\n⚠️ Ошибки:\n<pre>{error}</pre>"

    except Exception as e:
        response = f"❌ Ошибка при выполнении:\n<pre>{str(e)}</pre>"

    return response, builder

@router.message(CustomCommand.waiting_for_command)
async def execute_custom_command(message: types.Message, state: FSMContext):
    command = message.text
    response, _ = await run_command_and_prepare_response(command)

    await message.reply(response, parse_mode="HTML")
    await state.clear()

@router.message(CustomCommand.waiting_for_command_alt)
async def execute_custom_command_query(message: types.Message, state: FSMContext):
    command = message.text
    response, builder = await run_command_and_prepare_response(command, with_back_button=True)

    await message.reply(
        response,
        parse_mode="HTML",
        reply_markup=builder.as_markup(resize_keyboard=True) if builder else None
    )

    await state.clear()
