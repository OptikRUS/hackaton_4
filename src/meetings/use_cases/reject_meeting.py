from ..repos import AppointmentRepo, Meeting, SlotRepo
from ..constants import MeetingStatus
from ..exceptions import MeetingNotFoundError, MeetingIsApproveError


class RejectMeetingCase:
    """
    Кейс отклонения записи на консультацию
    """
    def __init__(
            self,
            slot_repo: type[SlotRepo],
            appointment_repo: type[AppointmentRepo],
    ) -> None:
        self.slot_repo: SlotRepo = slot_repo()
        self.appointment_repo: AppointmentRepo = appointment_repo()

    async def __call__(self, meeting_id: int, inspector_id: int) -> Meeting:
        meeting: Meeting = await self.appointment_repo.retrieve(
            filters=dict(id=meeting_id),
            prefetch_fields=["slot"]
        )
        if not meeting:
            raise MeetingNotFoundError
        if meeting.status == MeetingStatus.WAIT.value:
            raise MeetingIsApproveError

        meeting_data: dict = dict(
            inspector_id=inspector_id,
            start_url="",
            join_url="",
            status=MeetingStatus.REJECTED.value,
            is_approved=False,
        )
        meeting: Meeting = await self.appointment_repo.update(model=meeting, data=meeting_data)
        await self.slot_repo.update(model=meeting.slot, data=dict(is_open=True))
        return meeting
