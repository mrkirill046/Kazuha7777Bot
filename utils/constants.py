import json
import os

from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

config_file = open("config.json", "r")
config = json.load(config_file)
token = os.getenv("BOT_TOKEN")
log_filename = datetime.now().strftime("%d.%m.%Y-%H.%M.log")

enter_command_message = "Введите команду для выполнения:"
not_found_message = "❌ Команда не найдена"
shutdown_message = "Вы действительно хотите выключить компьютер?"
restart_message = "Вы действительно хотите перезагрузить компьютер?"
wait_message = "Пожалуйста, подождите..."
settings_message = "Выберите нужную вам настройку из меню ниже."
not_allowed_message = "Действие не было совершено! Необходимо получить полный доступ к боту."
error_message = "Прости, но что-то пошло не так. Действие не было совершено! Сожалею :("
command_message = "Выберите, что вы хотите сделать. Для этого нажмите на нужную вам кнопку."
welcome_message = """
Добро пожаловать в личного бота для @kazuha7777! \n
Выберите, что вы хотите сделать. Для этого нажмите на нужную вам кнопку.
"""

settings_button = "⚙️ Настройки"
user_button = "👤 Личный кабинет"
command_button = "🔧 Команды"
tgc_button = "💻 Мой ТГК"
back_command = "◀️ Назад"
no_restart_command = "❌ Нет, не уверен"
yes_restart_command = "✅ Да, уверен"
no_shutdown_command = "❌ Нет, не уверен"
yes_shutdown_command = "✅ Да, уверен"

HELLO_WORLD_CODES = {
    "python": 'print("Hello, world!")',
    "c++": '#include <iostream>\nint main() {\n    std::cout << "Hello, world!";\n    return 0;\n}',
    "java": 'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Hello, world!");\n    }\n}',
    "javascript": 'console.log("Hello, world!");',
    "rust": 'fn main() {\n    println!("Hello, world!");\n}',
}

BIO_TEXT = (
    "👤 Имя: `Кирилл`\n"
    "🎂 День рождения: `13.06.2010`\n"
    "💻 Программист, люблю кодить\n"
    "🏫 Учусь в школе `(9 класс)`\n"
)

LANG_LIST_MD = (
    "*💡 Укажите язык программирования:*\n\n"
    "- `python`\n"
    "- `c++`\n"
    "- `java`\n"
    "- `javascript`\n"
    "- `rust`"
)
