from enum import Enum


class MeetingStatus(str, Enum):
    WAIT = "waiting"
    NOT_APPROVE = "not_approve"
    REJECTED = "rejected"
