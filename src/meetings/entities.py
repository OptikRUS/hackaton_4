from pydantic import BaseModel

from common.orm import BaseRepo
from common.exceptions import BaseExceptionModel


class BaseMeetingModel(BaseModel):
    """
    Базовая модель сервиса ГИС
    """


class BaseMeetingRepo(BaseRepo):
    """
    Базовый репозиторий сервиса ГИС
    """


class BaseMeetingExceptionModel(BaseExceptionModel):
    """
    Базовая ошибка сервиса ГИС
    """