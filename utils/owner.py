from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message

from utils.constants import config, not_allowed_message


class OwnerOnlyMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: dict[str, Any],
    ) -> Any:
        user_id = event.from_user.id if event.from_user else None

        if user_id != config["owner_id"]:
            if isinstance(event, CallbackQuery):
                await event.answer(text=not_allowed_message, show_alert=True)
            else:
                await event.answer(text=not_allowed_message)

            return None

        return await handler(event, data)
