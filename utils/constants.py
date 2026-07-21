import json
import os
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

with open("config.json", "r") as f:
    config: dict = json.load(f)

token: str = os.getenv("BOT_TOKEN", "")
log_filename: str = datetime.now().strftime("%d.%m.%Y-%H.%M.log")

enter_command_message = "Enter the command to execute:"
not_found_message = "Command not found"
shutdown_message = "Are you sure you want to shut down the computer?"
restart_message = "Are you sure you want to restart the computer?"
wait_message = "Please wait..."
not_allowed_message = "Action denied. Full access to the bot is required."
error_message = "Something went wrong. The action was not completed."
command_message = "Choose what you want to do by pressing a button."
welcome_message = (
    "Welcome to the personal bot for @kazuha7777!\n\n"
    "Choose what you want to do by pressing a button."
)

user_button = "Profile"
command_button = "Commands"
tgc_button = "My TG Channel"
back_command = "Back"
no_restart_command = "No, not sure"
yes_restart_command = "Yes, confirm"
no_shutdown_command = "No, not sure"
yes_shutdown_command = "Yes, confirm"

HELLO_WORLD_CODES: dict[str, str] = {
    "python": 'print("Hello, world!")',
    "c++": '#include <iostream>\nint main() {\n    std::cout << "Hello, world!";\n    return 0;\n}',
    "java": 'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Hello, world!");\n    }\n}',
    "javascript": 'console.log("Hello, world!");',
    "rust": 'fn main() {\n    println!("Hello, world!");\n}',
}

BIO_TEXT = (
    "Name: `Kirill`\n"
    "Birthday: `13.06.2010`\n"
    "Programmer, love coding\n"
    "School student `(9th grade)`\n"
)

LANG_LIST_MD = (
    "*Specify a programming language:*\n\n"
    "- `python`\n"
    "- `c++`\n"
    "- `java`\n"
    "- `javascript`\n"
    "- `rust`"
)
