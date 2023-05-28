from datetime import datetime

from common.zoom import ZoomClient, ZoomMeeting
from ..repos import AppointmentRepo, Meeting
from ..exceptions import MeetingNotFoundError


class ApproveMeetingCase:
    """
    Кейс подтверждения записи на консультацию
    """
    def __init__(
            self,
            appointment_repo: type[AppointmentRepo],
            zoom_client: type[ZoomClient],
    ) -> None:
        self.appointment_repo: AppointmentRepo = appointment_repo()
        self.zoom_client: type[ZoomClient] = zoom_client

    async def __call__(self, meeting_id: int, inspector_id: int) -> Meeting:
        meeting: Meeting = await self.appointment_repo.retrieve(
            filters=dict(id=meeting_id),
            prefetch_fields=["topic", "slot"]
        )
        if not meeting:
            raise MeetingNotFoundError

        start_datetime: datetime = datetime.combine(meeting.slot.slot_date, meeting.slot.slot_time)
        zoom_meeting_data: dict = dict(
            topic=meeting.topic.name,
            start_time=str(start_datetime),
            duration_min=60,
            password='not-secure'
        )
        zoom_meeting: ZoomMeeting = self.zoom_client.meetings.create_meeting(**zoom_meeting_data)
        self.zoom_client.meetings.delete_meeting(meeting_id=zoom_meeting.id)  # ToDo пока встреча будет сразу удаляться
        meeting_data: dict = dict(
            inspector_id=inspector_id,
            start_url=zoom_meeting.start_url,
            join_url=zoom_meeting.join_url,
            status=zoom_meeting.status,
            is_approved=True,
        )
        meeting: Meeting = await self.appointment_repo.update(model=meeting, data=meeting_data)
        return meeting
