from aiogram.fsm.state import StatesGroup, State

class CustomCommand(StatesGroup):
    waiting_for_command = State()
    waiting_for_command_alt = State()
