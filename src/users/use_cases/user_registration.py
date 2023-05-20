from common.security import hasher
from src.users.models import UserRegisterRequest
from ..repos import UserRepo, User
from ..exceptions import UserAlreadyRegisteredError, UserEmailTakenError, UserPhoneTakenError
from ..maintenance import su_registration

from config import super_users_config


class UserRegistration:
    """
    Кейс регистрации пользователя
    """

    def __init__(self) -> None:
        self.hasher = hasher
        self.user_repo: UserRepo = UserRepo()

    @su_registration(super_users_config.get("superusers"))
    async def __call__(self, user: UserRegisterRequest) -> User:
        username_filters: dict = dict(username=user.username)

        username_exist: bool = await self.user_repo.exists(filters=username_filters)
        if username_exist:
            raise UserAlreadyRegisteredError

        user.password = self.hasher.hash(user.password)

        new_user: User = await self.user_repo.create(user.dict())
        return new_user
