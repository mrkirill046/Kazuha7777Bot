import uuid
import os
import requests

from aiogram import Router, types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultGif, InlineQueryResult
from utils import constants, config

router = Router()


@router.inline_query()
async def handle_inline_query(inline_query: types.InlineQuery):
    query = inline_query.query.strip().lower()
    results: list[InlineQueryResultArticle] = []

    if query.startswith("hw "):
        lang = query[3:].strip()
        code = constants.HELLO_WORLD_CODES.get(lang)

        if code:
            results.append(
                InlineQueryResultArticle(
                    id=str(uuid.uuid4()),
                    title=f"Hello World на {lang}",
                    description=f"Пример Hello World на {lang}",
                    input_message_content=InputTextMessageContent(
                        message_text=f"*💻 Hello World на {lang}:*\n\n```{lang}\n{code}\n```",
                        parse_mode="Markdown"
                    )
                )
            )
        else:
            results.append(
                InlineQueryResultArticle(
                    id=str(uuid.uuid4()),
                    title="Язык не найден",
                    description="Доступные: python, c++, java, javascript, rust",
                    input_message_content=InputTextMessageContent(
                        message_text="❌ Язык не найден. Пример: `hw python`",
                        parse_mode="Markdown"
                    )
                )
            )

    elif query == "hw":
        results.append(
            InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title="Укажите язык",
                description="Выберите один из доступных языков",
                input_message_content=InputTextMessageContent(
                    message_text=constants.LANG_LIST_MD,
                    parse_mode="Markdown"
                )
            )
        )

    elif query == "bio" and inline_query.from_user.id == config["owner_id"]:
        results.append(
            InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title="Моя биография",
                description="Информация о владельце",
                input_message_content=InputTextMessageContent(
                    message_text=constants.BIO_TEXT,
                    parse_mode="Markdown"
                )
            )
        )

    elif query == "gif":
        results.append(
            InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title="Введите поисковый запрос",
                description="Пример: gif кот",
                input_message_content=InputTextMessageContent(
                    message_text="❌ Пожалуйста, введите поисковый запрос после команды `gif`.",
                    parse_mode="Markdown"
                )
            )
        )

    elif query.startswith("gif "):
        search_term = query[4:].strip()

        api_key = os.getenv("TENOR_API_KEY")
        limit = 15

        response = requests.get(
            "https://tenor.googleapis.com/v2/search",
            params={
                "q": search_term,
                "key": api_key,
                "limit": limit,
                "media_filter": "minimal",
                "contentfilter": "medium"
            }
        )

        if response.status_code == 200:
            data = response.json()

            results: list[InlineQueryResult] = []

            for result in data.get("results", []):
                gif_url = result["media_formats"]["gif"]["url"]
                preview = result["media_formats"]["tinygif"]["url"]

                results.append(
                    InlineQueryResultGif(
                        id=str(uuid.uuid4()),
                        gif_url=gif_url,
                        thumbnail_url=preview,
                        title=search_term
                    )
                )
        else:
            results.append(
                InlineQueryResultArticle(
                    id=str(uuid.uuid4()),
                    title="Ошибка при поиске GIF",
                    description="Попробуйте позже",
                    input_message_content=InputTextMessageContent(
                        message_text="❌ Не удалось получить GIF. Пожалуйста, попробуйте позже.",
                        parse_mode="Markdown"
                    )
                )
            )

    elif query == "":
        results.append(
            InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title="hw <язык>",
                description="Показать Hello World на одном из языков",
                input_message_content=InputTextMessageContent(
                    message_text=constants.LANG_LIST_MD,
                    parse_mode="Markdown"
                )
            )
        )

        results.append(
            InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title="gif <запрос>",
                description="Найти и отправить гифку по запросу",
                input_message_content=InputTextMessageContent(
                    message_text="Введите `gif <что искать>` для поиска гифок!",
                    parse_mode="Markdown"
                )
            )
        )

        if inline_query.from_user.id == config["owner_id"]:
            results.append(
                InlineQueryResultArticle(
                    id=str(uuid.uuid4()),
                    title="bio",
                    description="Информация о владельце бота",
                    input_message_content=InputTextMessageContent(
                        message_text=constants.BIO_TEXT,
                        parse_mode="Markdown"
                    )
                )
            )

    await inline_query.answer(results, cache_time=0, is_personal=True)
