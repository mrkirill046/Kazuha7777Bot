import importlib
import logging
import pkgutil
from typing import TypedDict

from aiogram import Dispatcher


class CommandMeta(TypedDict):
    name: str
    description: str
    callback_data: str


def load_all_modules(dp: Dispatcher) -> tuple[list[CommandMeta], object | None]:
    commands: list[CommandMeta] = []
    not_found_router = None

    for _, module_name, _ in pkgutil.iter_modules(["modules"]):
        module = importlib.import_module(f"modules.{module_name}")

        if module_name == "not_found":
            not_found_router = module.router
            continue

        if hasattr(module, "router"):
            dp.include_router(module.router)
            logging.info("Module loaded: %s", module_name)

        if hasattr(module, "COMMAND_META"):
            commands.append(module.COMMAND_META)
            logging.info("Command registered: %s", module.COMMAND_META["name"])

    if not_found_router is not None:
        dp.include_router(not_found_router)
        logging.info("Module loaded: not_found (last)")

    return commands
