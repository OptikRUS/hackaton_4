from fastapi import APIRouter, Depends, Query

from common.security import UserAuth, UserType
from ..use_cases import GetAnswerCase
from ..services import BotAnswerService
from ..models import AnswerListResponse

router: APIRouter = APIRouter(prefix="/chat-bot", tags=["chat bot"])


@router.get(
    "/answer",
    dependencies=[Depends(UserAuth(UserType.CLIENT))],
    response_model=AnswerListResponse,
)
async def get_bot_answer_view(query: str = Query(..., description="Вопрос в чате")):
    """
    Получение ответа в чате
    """
    resources: dict = dict(
        bot_answer_service=BotAnswerService,
    )
    get_answer: GetAnswerCase = GetAnswerCase(**resources)
    return await get_answer(query=query)
