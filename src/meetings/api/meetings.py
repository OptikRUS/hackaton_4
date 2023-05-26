from fastapi import APIRouter, Depends, Query

from common.security import UserAuth, UserType
from src.meetings.repos import SlotRepo, AppointmentRepo
from src.users.repos import User
from ..use_cases import ReserveSlotCase
from ..models import Appointments

router: APIRouter = APIRouter(prefix="/meetings", tags=["meetings"])


@router.post(
    "/reserve",
    response_model=Appointments,
)
async def reserve_slot_view(
        slot_id: int = Query(..., description="slot_id"),
        user: User = Depends(UserAuth(UserType.CLIENT)),
):
    """
    Запись на консультацию
    """
    resources: dict = dict(
        slot_repo=SlotRepo,
        appointment_repo=AppointmentRepo,
    )
    reserve_slot: ReserveSlotCase = ReserveSlotCase(**resources)
    return await reserve_slot(slot_id=slot_id, user_id=user.id)
