from pydantic import BaseModel

from common.orm import BaseRepo
from common.exceptions import BaseExceptionModel


class BaseGisServiceModel(BaseModel):
    """
    Базовая модель сервиса ГИС
    """


class BaseGisServiceRepo(BaseRepo):
    """
    Базовый репозиторий сервиса ГИС
    """


class BaseGisServiceExceptionModel(BaseExceptionModel):
    """
    Базовая ошибка сервиса ГИС
    """