from datetime import date, time

from ..entities import BaseCounselingModel


class Slot(BaseCounselingModel):
    id: int
    slot_date: date
    slot_time: time


class Supervision(BaseCounselingModel):
    id: int
    name: str


class SlotListResponse(BaseCounselingModel):
    id: int
    name: str
    open_slots: list[Slot]

    class Config:
        orm_mode = True
