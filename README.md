# Telegram Bot на Aiogram — Персональный Ассистент Казухи 🚀🤖

[![Python](https://img.shields.io/badge/python-3.13%2B-blue?logo=python&style=for-the-badge)](https://www.python.org/)
[![Aiogram](https://img.shields.io/badge/aiogram-3.x-blue?logo=python&style=for-the-badge)](https://docs.aiogram.dev/en/latest/)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/status-development-yellow?style=for-the-badge)]()

---

## Описание

Это персональный Telegram-бот, написанный на Python с использованием библиотеки [Aiogram](https://docs.aiogram.dev/), который управляет моим компьютером и выполняет различные полезные команды.

**Главные фишки:**

- Управление компьютером через Telegram (открытие программ, запуск скриптов, и т.п.)
- Выполнение системных команд удалённо
- Все зависимости вынесены в `requirements.txt`

---

## Быстрый старт 🚀

### 1. Клонируй репозиторий

```bash
git clone https://github.com/mrkirill046/Kazuha7777Bot.git
cd Kazuha7777Bot
```

### 2. Создай и активируй виртуальное окружение

```fish
uv venv
source .venv/bin/activate.fish
```

*Если используешь bash/zsh:*

```bash
uv venv
source .venv/bin/activate
```

### 3. Создай `.env` файл с настройками бота

```env
BOT_TOKEN=твой_токен_от_бота_в_Telegram
TENOR_API_KEY=твой_токен_от_Tenor
```

### 4. Настройки бота в `config.json`

### 5. Запусти бота

```bash
uv run --script bot.py
```

---

## Структура проекта

```
.
├── assets/             # Файлы ресурсов: картинки, аудио, видео, файлы и т.п.
├── modules/            # Модули бота — обработчики, команды и расширения
├── utils/              # Утилиты и вспомогательные функции
│
├── config.json         # Конфигурационный файл с токенами и настройками
├── .env                # Конфиденциальные настройки (не в репозитории!)
├── pyproject.toml      # Файл зависимостей
├── README.md           # Документация проекта (ты её читаешь 😉)
└── bot.py              # Главный запускной файл бота
```

---

## Команды (Arch Linux - Hyprland)

| Команда       | Описание                                       |
|---------------|------------------------------------------------|
| `/start`      | Запуск бота                                    |
| `/shutdown`   | Выключение компьютера                          |
| `/restart`    | Перезагрузка компьютера                        |
| `/status`     | Проверка состояния компьютера                  |
| `/screenshot` | Скриншот активного экрана                      |
| `/custom`     | Выполняет пользовательскую команду в терминале |

---

## ПРЕДУПРЕЖДЕНИЕ
Для работы скриншотов у вас должен быть `grimblast` (отредактируйте его путь в `utils/pc_manage.py` в методе `screenshot`)

Также бот должен быть запущен как юзер-сервис
```bash
nano ~/.config/systemd/user/kazuha7777bot.service
```

#### !!! Не забудьте поменять пути !!!

```ini
[Unit]
Description=Kazuha7777 Telegram Bot
After=network.target

[Service]
WorkingDirectory=/home/mrkir/Documents/Python/kazuha7777Bot
ExecStart=/home/mrkir/.local/bin/uv run --project /home/mrkir/Documents/Python/kazuha7777Bot --script /home/mrkir/Documents/Python/kazuha7777Bot/bot.py
Restart=always
RestartSec=10
Environment=XDG_RUNTIME_DIR=/run/user/1000
Environment=WAYLAND_DISPLAY=wayland-1
Environment=PATH=/home/mrkir/Documents/Python/kazuha7777Bot/.venv/bin:/usr/bin:/bin
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=default.target
```

#### Запуск

```bash
systemctl --user daemon-reload                 
systemctl --user enable --now kazuha7777bot.service
```

---

## Лицензия

Этот проект под лицензией MIT — пользуйся, модифицируй и распространяй свободно!

---

## Контакты

Если хочешь что-то улучшить или добавить — пиши!
Telegram: [@kazuha7777](https://t.me/kazuha7777)

---

# Спасибо за внимание
