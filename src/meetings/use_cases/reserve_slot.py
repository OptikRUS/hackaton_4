from ..repos import SlotRepo, Slot, AppointmentRepo, Appointment


class ReserveSlotCase:
    """
    Кейс записи на консультацию
    """
    def __init__(
            self,
            slot_repo: type[SlotRepo],
            appointment_repo: type[AppointmentRepo],
    ) -> None:
        self.slot_repo: SlotRepo = slot_repo()
        self.appointment_repo: AppointmentRepo = appointment_repo()

    async def __call__(self, slot_id: int, user_id: int) -> Appointment:
        filters: dict = dict(slot_id=slot_id, user_id=user_id)
        appointment_reserved: bool = await self.appointment_repo.exists(filters=filters)
        if appointment_reserved:
            print("Ошибка! Слот уже забронирован")

        slot: Slot = await self.slot_repo.retrieve(filters=dict(id=slot_id))
        appointment_data: dict = dict(user_id=user_id, slot_id=slot.id)
        appointment: Appointment = await self.appointment_repo.create(data=appointment_data)
        await self.slot_repo.update(model=slot, data=dict(is_open=False))
        return appointment
