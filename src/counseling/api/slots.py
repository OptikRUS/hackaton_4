from fastapi import APIRouter, Depends, Query

from common.security import UserAuth, UserType
from src.users.repos import User
from src.meetings.repos import SlotRepo
from ..use_cases import GetOpenSlotListCase, GetClosedSlotListCase, GetApprovedSlotListCase
from ..models import Slot

router: APIRouter = APIRouter(prefix="/slots", tags=["slots"])


@router.get(
    "/opened_list",
    dependencies=[Depends(UserAuth(UserType.CLIENT))],
    response_model=list[Slot],
)
async def get_opened_slot_list_view(
        inspector: User = Depends(UserAuth(UserType.INSPECTOR))
):
    """
    Получение списка свободных слотов для инспектора КНО
    """
    resources: dict = dict(
        slot_repo=SlotRepo,
    )
    get_open_slots: GetOpenSlotListCase = GetOpenSlotListCase(**resources)
    return await get_open_slots(inspector=inspector)


@router.get(
    "/closed_list",
    dependencies=[Depends(UserAuth(UserType.CLIENT))],
    response_model=list[Slot],
)
async def get_closed_slot_list_view(
        inspector: User = Depends(UserAuth(UserType.INSPECTOR))
):
    """
    Получение списка слотов зарезервированных пользователем для инспектора КНО
    """
    resources: dict = dict(
        slot_repo=SlotRepo,
    )
    get_open_slots: GetClosedSlotListCase = GetClosedSlotListCase(**resources)
    return await get_open_slots(inspector=inspector)


@router.get(
    "/approved_list",
    dependencies=[Depends(UserAuth(UserType.CLIENT))],
    response_model=list[Slot],
)
async def get_approved_slot_list_view(
        inspector: User = Depends(UserAuth(UserType.INSPECTOR))
):
    """
    Получение списка слотов подтвержденных инспектором КНО
    """
    resources: dict = dict(
        slot_repo=SlotRepo,
    )
    get_open_slots: GetApprovedSlotListCase = GetApprovedSlotListCase(**resources)
    return await get_open_slots(inspector=inspector)
