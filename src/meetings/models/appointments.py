from ..entities import BaseMeetingModel


class Appointments(BaseMeetingModel):
    id: int
    slot_id: int
    user_id: int
