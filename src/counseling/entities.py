from pydantic import BaseModel

from common.orm import BaseRepo
from common.exceptions import BaseExceptionModel


class BaseCounselingModel(BaseModel):
    """
    Базовая модель сервиса ГИС
    """


class BaseCounselingRepo(BaseRepo):
    """
    Базовый репозиторий сервиса ГИС
    """


class BaseCounselingExceptionModel(BaseExceptionModel):
    """
    Базовая ошибка сервиса ГИС
    """
