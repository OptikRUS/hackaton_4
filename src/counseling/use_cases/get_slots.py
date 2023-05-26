from tortoise.queryset import QuerySet

from src.meetings.repos import SlotRepo
from ..repos import Supervisor, SupervisorRepo


class GetSlotsCase:
    """
    Кейс получения свободных слотов
    """
    def __init__(
            self,
            supervisor_repo: type[SupervisorRepo],
            slot_repo: type[SlotRepo],
    ) -> None:
        self.supervisor_repo: SupervisorRepo = supervisor_repo()
        self.slot_repo: SlotRepo = slot_repo()

    async def __call__(self, supervisor_id: int) -> Supervisor:
        slots_qs: QuerySet = self.slot_repo.list(filters=dict(is_open=True))
        supervisor: Supervisor = await self.supervisor_repo.retrieve(
            filters=dict(id=supervisor_id),
            prefetch_fields=[
                dict(relation="slots", queryset=slots_qs, to_attr="open_slots")
            ]
        )

        return supervisor
