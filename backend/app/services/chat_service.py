from __future__ import annotations
import logging

from openai import OpenAI

from app.core.config import settings
from app.services.context_guard import is_in_scope, out_of_scope_answer
from app.services.prompt_builder import build_messages

logger = logging.getLogger(__name__)


class ChatService:
    def __init__(self) -> None:
        self.client = OpenAI(api_key=settings.openai_api_key) if settings.openai_api_key else None

    def answer(self, message: str, history: list[dict]) -> tuple[str, bool]:
        if not is_in_scope(message, history):
            return out_of_scope_answer(), False

        if not self.client:
            return (
                "El servicio está listo, pero falta configurar OPENAI_API_KEY para generar respuestas con ChatGPT.",
                True,
            )

        messages = build_messages(message, history)
        try:
            response = self.client.chat.completions.create(
                model=settings.openai_model,
                messages=messages,
                temperature=0.3,
            )
            content = response.choices[0].message.content or "No pude generar una respuesta en este momento."
            return content, True
        except Exception:
            logger.exception("OpenAI chat request failed")
            return (
                "El servicio tuvo un problema temporal al consultar ChatGPT. Intenta de nuevo en unos segundos.",
                True,
            )
