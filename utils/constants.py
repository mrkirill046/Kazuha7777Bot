import json
import os

from dotenv import load_dotenv

load_dotenv()

config_file = open("config.json", "r")
config = json.load(config_file)
token = os.getenv("BOT_TOKEN")
