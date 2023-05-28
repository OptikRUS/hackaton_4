from fastapi import APIRouter, Depends, Query

from common.security import UserAuth, UserType
from src.meetings.repos import SlotRepo
from ..use_cases import GetSlotListCase
from ..repos import SupervisorRepo
from ..models import SlotListResponse

router: APIRouter = APIRouter(prefix="/slots", tags=["slots"])


@router.get(
    "/list",
    dependencies=[Depends(UserAuth(UserType.CLIENT))],
    response_model=SlotListResponse,
)
async def get_slot_list_view(supervisor_id: int = Query(..., description="supervisor_id")):
    """
    Получение списка свободных слотов для КНО
    """
    resources: dict = dict(
        supervisor_repo=SupervisorRepo,
        slot_repo=SlotRepo,
    )
    get_slots: GetSlotListCase = GetSlotListCase(**resources)
    return await get_slots(supervisor_id=supervisor_id)
