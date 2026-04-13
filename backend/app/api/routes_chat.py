from fastapi import APIRouter, Depends

from app.api.deps import get_chat_service
from app.models.schemas import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter(prefix="/api/chat", tags=["chat"])


@router.post("", response_model=ChatResponse)
def chat(payload: ChatRequest, chat_service: ChatService = Depends(get_chat_service)) -> ChatResponse:
    answer, in_scope = chat_service.answer(
        message=payload.message,
        history=[m.model_dump() for m in payload.history],
    )
    return ChatResponse(answer=answer, in_scope=in_scope)
