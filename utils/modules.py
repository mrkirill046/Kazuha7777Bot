import importlib
import pkgutil
import logging

from aiogram import Dispatcher

def load_all_modules(dp: Dispatcher):
    for _, module_name, _ in pkgutil.iter_modules(["modules"]):
        module = importlib.import_module(f"modules.{module_name}")

        if hasattr(module, "router"):
            dp.include_router(module.router)
            logging.info(f"Module loaded: {module_name}")
