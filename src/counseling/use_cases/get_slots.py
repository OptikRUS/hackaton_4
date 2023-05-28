from src.meetings.repos import SlotRepo, Slot
from src.meetings.constants import MeetingStatus
from src.users.repos import User


class GetOpenSlotListCase:
    """
    Кейс получения свободных слотов
    """
    def __init__(
            self,
            slot_repo: type[SlotRepo],
    ) -> None:
        self.slot_repo: SlotRepo = slot_repo()

    async def __call__(self, inspector: User) -> list[Slot]:
        slot_filters: dict = dict(is_open=True, supervisor_id=inspector.supervisor_id)
        return await self.slot_repo.list(filters=slot_filters)


class GetClosedSlotListCase:
    """
    Кейс слотов зарезервированных пользователем
    """
    def __init__(
            self,
            slot_repo: type[SlotRepo],
    ) -> None:
        self.slot_repo: SlotRepo = slot_repo()

    async def __call__(self, inspector: User) -> list[Slot]:
        slot_filters: dict = dict(is_open=False, supervisor_id=inspector.supervisor_id)
        return await self.slot_repo.list(filters=slot_filters)


class GetApprovedSlotListCase:
    """
    Кейс слотов подтвержденных инспектором КНО
    """
    def __init__(
            self,
            slot_repo: type[SlotRepo],
    ) -> None:
        self.slot_repo: SlotRepo = slot_repo()

    async def __call__(self, inspector: User) -> list[Slot]:
        slot_filters: dict = dict(
            is_open=False,
            supervisor_id=inspector.supervisor_id,
            meeting__status=MeetingStatus.WAIT.value,
        )
        return await self.slot_repo.list(filters=slot_filters)
