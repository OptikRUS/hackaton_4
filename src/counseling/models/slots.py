from datetime import date, time

from pydantic import validator

from ..entities import BaseCounselingModel


class Slot(BaseCounselingModel):
    id: int
    slot_date: date
    slot_time: time

    @validator("slot_time")
    def slot_time_validate(cls, slot_time):
        return f"{slot_time.hour}:00 - {slot_time.hour + 1}:00"


class SlotListResponse(BaseCounselingModel):
    id: int
    name: str
    open_slots: list[Slot]

    class Config:
        orm_mode = True
