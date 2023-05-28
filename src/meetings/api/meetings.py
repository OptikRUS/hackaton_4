from fastapi import APIRouter, Depends, Query, Path

from common.security import UserAuth, UserType
from common.zoom import zoom_client
from src.meetings.repos import SlotRepo, AppointmentRepo
from src.counseling.repos import TopicRepo
from src.users.repos import User
from ..use_cases import ReserveSlotCase, ApproveMeetingCase, RejectMeetingCase
from ..models import Meeting, ApprovedMeeting

router: APIRouter = APIRouter(prefix="/meetings", tags=["meetings"])


@router.post("/reserve", response_model=Meeting)
async def reserve_slot_view(
        slot_id: int = Query(..., description="slot_id"),
        topic_id: int = Query(..., description="topic_id"),
        user: User = Depends(UserAuth(UserType.CLIENT))
):
    """
    Запись на консультацию
    """
    resources: dict = dict(
        slot_repo=SlotRepo,
        appointment_repo=AppointmentRepo,
        topic_repo=TopicRepo,
    )
    reserve_slot: ReserveSlotCase = ReserveSlotCase(**resources)
    return await reserve_slot(slot_id=slot_id, topic_id=topic_id, user_id=user.id)


@router.patch("/approve/{meeting_id}", response_model=ApprovedMeeting)
async def approve_meeting_view(
        meeting_id: int = Path(..., description="appointment_id"),
        inspector: User = Depends(UserAuth(UserType.INSPECTOR))
):
    """
    Подтверждение записи на консультацию
    """
    resources: dict = dict(
        appointment_repo=AppointmentRepo,
        zoom_client=zoom_client,
    )
    approve_meeting: ApproveMeetingCase = ApproveMeetingCase(**resources)
    return await approve_meeting(meeting_id=meeting_id, inspector_id=inspector.id)


@router.patch(
    "/reject/{meeting_id}",
    response_model=ApprovedMeeting,
)
async def reject_meeting_view(
        meeting_id: int = Path(..., description="meeting_id_id"),
        inspector: User = Depends(UserAuth(UserType.INSPECTOR)),
):
    """
    Отклонения записи на консультацию
    """
    resources: dict = dict(
        slot_repo=SlotRepo,
        appointment_repo=AppointmentRepo,
    )
    reject_meeting: RejectMeetingCase = RejectMeetingCase(**resources)
    return await reject_meeting(meeting_id=meeting_id, inspector_id=inspector.id)
