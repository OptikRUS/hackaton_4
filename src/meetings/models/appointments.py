from ..entities import BaseMeetingModel


class Meeting(BaseMeetingModel):
    id: int
    slot_id: int
    user_id: int
    status: str
    is_approved: bool


class ApprovedMeeting(Meeting):
    inspector_id: int
    start_url: str
    join_url: str
    is_approved: bool
