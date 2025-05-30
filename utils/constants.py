import json
import os

from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

config_file = open("config.json", "r")
config = json.load(config_file)
token = os.getenv("BOT_TOKEN")
log_filename = datetime.now().strftime("%d.%m.%Y-%H.%M.log")

welcome_message = """
Добро пожаловать в личного бота для @kazuha7777! \n
Выберите, что вы хотите сделать. Для этого нажмите на нужную вам кнопку.
"""

settings_button = "⚙️ Настройки"
user_button = "👤 Личный кабинет"
command_button = "🔧 Команды"
tgc_button = "💻 Мой ТГК"
