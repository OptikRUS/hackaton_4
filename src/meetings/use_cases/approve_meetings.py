from datetime import datetime

from common.zoom import ZoomClient, ZoomMeeting
from ..repos import AppointmentRepo, Appointment


class ApproveMeetingsCase:
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

    async def __call__(self, appointment_id: int, inspector_id: int) -> Appointment:
        appointment: Appointment = await self.appointment_repo.retrieve(
            filters=dict(id=appointment_id),
            prefetch_fields=["topic", "slot"]
        )
        if not appointment:
            print("Ошибка: Консультация не найдена")

        start_datetime: datetime = datetime.combine(appointment.slot.slot_date, appointment.slot.slot_time)
        zoom_meeting_data: dict = dict(
            topic=appointment.topic.name,
            start_time=str(start_datetime),
            duration_min=30,
            password='not-secure'
        )
        zoom_meeting: ZoomMeeting = self.zoom_client.meetings.create_meeting(**zoom_meeting_data)
        self.zoom_client.meetings.delete_meeting(meeting_id=zoom_meeting.id)  # ToDo пока встреча будет сразу удаляться
        appointment_data: dict = dict(
            inspector_id=inspector_id,
            start_url=zoom_meeting.start_url,
            join_url=zoom_meeting.join_url,
            status=zoom_meeting.status,
            is_approved=True,
        )
        appointment: Appointment = await self.appointment_repo.update(model=appointment, data=appointment_data)
        return appointment
