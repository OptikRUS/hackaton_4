from ..repos import AppointmentRepo, Appointment, SlotRepo
from ..constants import MeetingStatus


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

    async def __call__(self, appointment_id: int, inspector_id: int) -> Appointment:
        appointment: Appointment = await self.appointment_repo.retrieve(
            filters=dict(id=appointment_id),
            prefetch_fields=["slot"]
        )
        if appointment.status == "waiting":
            print("Ошибка: Консультация уже подтверждена")

        if not appointment:
            print("Ошибка: Консультация не найдена")

        appointment_data: dict = dict(
            inspector_id=inspector_id,
            start_url="",
            join_url="",
            status=MeetingStatus.REJECTED.value,
            is_approved=False,
        )
        appointment: Appointment = await self.appointment_repo.update(model=appointment, data=appointment_data)
        await self.slot_repo.update(model=appointment.slot, data=dict(is_open=True))
        return appointment
