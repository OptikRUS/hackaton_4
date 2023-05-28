from common.exceptions import BaseNotFoundError


class SlotNotFoundError(BaseNotFoundError):
    message: str = "Свободный слот не найден."
    reason: str = "slot_not_found_error"


class TopicNotFoundError(BaseNotFoundError):
    message: str = "Тема консультирования не найдена."
    reason: str = "topic_not_found_error"


class MeetingNotFoundError(BaseNotFoundError):
    message: str = "Запись на консультацию не найдена."
    reason: str = "meeting_not_found_error"


class MeetingIsApproveError(BaseNotFoundError):
    message: str = "Запись на консультацию уже была одобрена."
    reason: str = "meeting_is_approved_error"
