# Kazuha7777 Bot

[![Python](https://img.shields.io/badge/python-3.13%2B-blue?logo=python&style=for-the-badge)](https://www.python.org/)
[![Aiogram](https://img.shields.io/badge/aiogram-3.x-blue?logo=python&style=for-the-badge)](https://docs.aiogram.dev/en/latest/)
[![NixOS](https://img.shields.io/badge/NixOS-26.11-blue?style=for-the-badge&logo=nixos)](https://nixos.org/)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)

Personal Telegram bot for remote computer management. Built with Python and Aiogram 3, designed for **NixOS + niri**.

## Features

- Remote PC control (shutdown, restart, status)
- Screenshot capture via niri (`niri msg action screenshot-screen`)
- Custom terminal command execution
- Inline queries (Hello World snippets, GIF search, bio)
- Self-registering commands — add a new command by dropping a module in `modules/`, no config changes needed

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager
- NixOS with niri compositor

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/mrkirill046/Kazuha7777Bot.git
cd Kazuha7777Bot
```

### 2. Set up the environment

```bash
uv venv
source .venv/bin/activate
```

### 3. Create `.env` file

```env
BOT_TOKEN=your_bot_token
TENOR_API_KEY=your_tenor_api_key
```

### 4. Set your Telegram user ID in `config.json`

```json
{
  "owner_id": 123456789
}
```

### 5. Run the bot

```bash
uv run --script bot.py
```

## Project Structure

```
.
├── assets/             # Static resources (images, audio, etc.)
├── modules/            # Bot handlers and features
│   ├── start.py        # /start command
│   ├── shutdown.py     # /shutdown command
│   ├── restart.py      # /restart command
│   ├── status.py       # /status command
│   ├── screenshot.py   # /screenshot command
│   ├── custom.py       # /custom command
│   ├── inline.py       # Inline query handlers
│   ├── keyboard.py     # Keyboard button handlers
│   ├── back.py         # Navigation handlers
│   └── not_found.py    # Unknown command handler
├── utils/              # Utilities and helpers
│   ├── constants.py    # Config, messages, constants
│   ├── modules.py      # Auto-module loader + command registry
│   ├── menu.py         # Keyboard builder
│   ├── owner.py        # Owner-only middleware
│   ├── pc_manage.py    # System commands (reboot, shutdown, screenshot)
│   ├── pc_status.py    # System info functions
│   └── state.py        # FSM states
├── config.json         # Bot configuration (owner_id only)
├── .env                # Secrets (not in repo)
├── pyproject.toml      # Dependencies
├── bot.py              # Entry point
└── README.md
```

## Adding a New Command

Create a new file in `modules/` with a `router` and an optional `COMMAND_META` dict:

```python
from aiogram import Router, types, F

router = Router()

COMMAND_META = {"name": "My Command", "description": "Does something", "callback_data": "my_command"}


@router.callback_query(F.data == "my_command")
async def handle(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text("Done!")
```

The module will be auto-loaded and the command will appear in the commands menu. No changes to `config.json` or any other file required.

## Commands

| Command      | Description                              |
|--------------|------------------------------------------|
| `/start`     | Start the bot                            |
| `/shutdown`  | Shut down the computer                   |
| `/restart`   | Restart the computer                     |
| `/status`    | Show computer status                     |
| `/screenshot`| Take a screenshot of the active screen   |
| `/custom`    | Run a custom terminal command            |

## Running as a systemd Service

```ini
[Unit]
Description=Kazuha7777 Telegram Bot
After=network.target

[Service]
WorkingDirectory=/path/to/kazuha7777Bot
ExecStart=/path/to/uv run --project /path/to/kazuha7777Bot --script /path/to/kazuha7777Bot/bot.py
Restart=always
RestartSec=10
Environment=WAYLAND_DISPLAY=wayland-1
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=default.target
```

```bash
systemctl --user daemon-reload
systemctl --user enable --now kazuha7777bot.service
```

## License

MIT — see [LICENSE](LICENSE)
