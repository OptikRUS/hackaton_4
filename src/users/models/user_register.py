from datetime import datetime

from pydantic import BaseModel, Field, Extra, SecretStr


class UserRegisterRequest(BaseModel):
    """
    Модель запроса регистрации пользователя
    """

    username: str = Field("username", min_length=3, max_length=20)
    password: str = Field("password123", max_length=128)

    # для добавления is_superuser = True в @su_registration
    class Config:
        extra = Extra.allow


class UserRegisterResponse(UserRegisterRequest):
    """
    Модель ответа регистрации пользователя
    """
    username: str = Field(...)
    password: SecretStr = Field(None, exclude=True)

    class Config:
        orm_mode = True
