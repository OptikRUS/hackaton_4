from pydantic import BaseModel, Field


class UserUpdateRequest(BaseModel):
    """
    Модель запроса изменения пользователя
    """

    username: str = Field("username", min_length=3, max_length=20)
