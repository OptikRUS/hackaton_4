from common.exceptions import (
    BaseNotAuthError,
    BaseForbiddenError,
    BaseNotFoundError,
    BaseConflictError
)


class UserTokenTimeOutError(BaseNotAuthError):
    message: str = "Время кода истекло."
    reason: str = "user_token_timeout"


class UserWrongPasswordError(BaseNotAuthError):
    message: str = "Введён неверный пароль."
    reason: str = "user_wrong_password"


class UserNotAuthError(BaseConflictError):
    message: str = "Пользователь не авторизован."
    reason: str = "user_not_auth"


class UserNotActiveError(BaseForbiddenError):
    message: str = "Пользователь неактивен."
    reason: str = 'user_not_active'
    headers: dict = {"WWW-Authenticate": "Bearer"}


class UserForbiddenError(BaseForbiddenError):
    message: str = "У пользователя нет прав."
    reason: str = 'user_forbidden_error'
