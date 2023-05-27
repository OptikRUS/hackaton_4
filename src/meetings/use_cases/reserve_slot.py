from src.counseling.repos import TopicRepo, Topic
from ..repos import SlotRepo, Slot, AppointmentRepo, Appointment


class ReserveSlotCase:
    """
    Кейс записи на консультацию
    """
    def __init__(
            self,
            slot_repo: type[SlotRepo],
            appointment_repo: type[AppointmentRepo],
            topic_repo: type[TopicRepo],
    ) -> None:
        self.slot_repo: SlotRepo = slot_repo()
        self.appointment_repo: AppointmentRepo = appointment_repo()
        self.topic_repo: TopicRepo = topic_repo()

    async def __call__(self, slot_id: int, topic_id: int, user_id: int) -> Appointment:
        slot: Slot = await self.slot_repo.retrieve(filters=dict(id=slot_id, is_open=True))
        if not slot:
            print("Ошибка: Свободный слот не найден")
        topic: Topic = await self.topic_repo.retrieve(filters=dict(id=topic_id))
        if not topic:
            print("Ошибка: Тема консультации не найдена")

        appointment_data: dict = dict(
            user_id=user_id,
            slot_id=slot.id,
            topic_id=topic.id,
            status="not_approve",
        )
        appointment: Appointment = await self.appointment_repo.create(data=appointment_data)
        await self.slot_repo.update(model=slot, data=dict(is_open=False))
        return appointment
