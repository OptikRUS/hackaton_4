from fastapi import APIRouter, Depends

from common.security import UserAuth, UserType
from ..use_cases import GetTopicListCase
from ..repos import TopicRepo
from ..models import Topic

router: APIRouter = APIRouter(prefix="/topics", tags=["topics"])


@router.get(
    "/list",
    response_model=list[Topic],
    dependencies=[Depends(UserAuth(UserType.CLIENT))],
)
async def get_topic_list_view():
    """
    Получение списка тем консультирования
    """
    resources: dict = dict(
        topic_repo=TopicRepo,
    )
    get_topics: GetTopicListCase = GetTopicListCase(**resources)
    return await get_topics()
