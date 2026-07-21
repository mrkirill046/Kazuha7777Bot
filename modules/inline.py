import os
import uuid

import requests
from aiogram import Router, types
from aiogram.types import (
    InlineQueryResult,
    InlineQueryResultArticle,
    InlineQueryResultGif,
    InputTextMessageContent,
)

from utils import config, constants

router = Router()


@router.inline_query()
async def handle_inline_query(inline_query: types.InlineQuery) -> None:
    query = inline_query.query.strip().lower()
    results: list[InlineQueryResultArticle] = []

    if query.startswith("hw "):
        lang = query[3:].strip()
        code = constants.HELLO_WORLD_CODES.get(lang)

        if code:
            results.append(
                InlineQueryResultArticle(
                    id=str(uuid.uuid4()),
                    title=f"Hello World in {lang}",
                    description=f"Hello World example in {lang}",
                    input_message_content=InputTextMessageContent(
                        message_text=f"*Hello World in {lang}:*\n\n```{lang}\n{code}\n```",
                        parse_mode="Markdown",
                    ),
                )
            )
        else:
            results.append(
                InlineQueryResultArticle(
                    id=str(uuid.uuid4()),
                    title="Language not found",
                    description="Available: python, c++, java, javascript, rust",
                    input_message_content=InputTextMessageContent(
                        message_text="Language not found. Example: `hw python`",
                        parse_mode="Markdown",
                    ),
                )
            )
    elif query == "hw":
        results.append(
            InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title="Specify language",
                description="Choose from available languages",
                input_message_content=InputTextMessageContent(
                    message_text=constants.LANG_LIST_MD,
                    parse_mode="Markdown",
                ),
            )
        )
    elif query == "bio" and inline_query.from_user.id == config["owner_id"]:
        results.append(
            InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title="My bio",
                description="Owner information",
                input_message_content=InputTextMessageContent(
                    message_text=constants.BIO_TEXT,
                    parse_mode="Markdown",
                ),
            )
        )
    elif query == "gif":
        results.append(
            InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title="Enter a search query",
                description="Example: gif cat",
                input_message_content=InputTextMessageContent(
                    message_text="Enter a search query after the `gif` command.",
                    parse_mode="Markdown",
                ),
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
                "contentfilter": "medium",
            },
            timeout=10,
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
                        title=search_term,
                    )
                )
        else:
            results.append(
                InlineQueryResultArticle(
                    id=str(uuid.uuid4()),
                    title="Error searching GIF",
                    description="Try again later",
                    input_message_content=InputTextMessageContent(
                        message_text="Failed to fetch GIF. Please try again later.",
                        parse_mode="Markdown",
                    ),
                )
            )
    elif query == "":
        results.append(
            InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title="hw <language>",
                description="Show Hello World in one of the languages",
                input_message_content=InputTextMessageContent(
                    message_text=constants.LANG_LIST_MD,
                    parse_mode="Markdown",
                ),
            )
        )

        results.append(
            InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title="gif <query>",
                description="Find and send a GIF by query",
                input_message_content=InputTextMessageContent(
                    message_text="Type `gif <search term>` to search for GIFs!",
                    parse_mode="Markdown",
                ),
            )
        )

        if inline_query.from_user.id == config["owner_id"]:
            results.append(
                InlineQueryResultArticle(
                    id=str(uuid.uuid4()),
                    title="bio",
                    description="Bot owner information",
                    input_message_content=InputTextMessageContent(
                        message_text=constants.BIO_TEXT,
                        parse_mode="Markdown",
                    ),
                )
            )

    await inline_query.answer(results, cache_time=0, is_personal=True)
