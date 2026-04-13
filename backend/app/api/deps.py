from functools import lru_cache

from app.services.chat_service import ChatService


@lru_cache
def get_chat_service() -> ChatService:
    return ChatService()
