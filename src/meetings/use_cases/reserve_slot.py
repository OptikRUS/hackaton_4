from src.counseling.repos import TopicRepo, Topic
from ..repos import SlotRepo, Slot, AppointmentRepo, Meeting
from ..constants import MeetingStatus
from ..exceptions import SlotNotFoundError, TopicNotFoundError


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

    async def __call__(self, slot_id: int, topic_id: int, user_id: int) -> Meeting:
        slot: Slot = await self.slot_repo.retrieve(filters=dict(id=slot_id, is_open=True))
        if not slot:
            raise SlotNotFoundError
        topic: Topic = await self.topic_repo.retrieve(filters=dict(id=topic_id))
        if not topic:
            raise TopicNotFoundError

        meeting_data: dict = dict(
            user_id=user_id,
            slot_id=slot.id,
            topic_id=topic.id,
            status=MeetingStatus.NOT_APPROVE.value,
        )
        meeting: Meeting = await self.appointment_repo.create(data=meeting_data)
        await self.slot_repo.update(model=slot, data=dict(is_open=False))
        return meeting
