from fastapi import Body

from ..entities import BaseMeetingModel


class SlotReserveRequest(BaseMeetingModel):
    slot_id: int = Body(..., description="slot_id")
    topic_id: int = Body(..., description="topic_id")
