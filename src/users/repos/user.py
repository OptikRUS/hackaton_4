from tortoise import fields
from tortoise.models import Model

from common.orm.mixins import GenericMixin
from ..entities import BaseUserRepo
from ..constants import UserRole


class User(Model):
    """
    Модель пользователя
    """
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(max_length=128, null=True)
    is_active = fields.BooleanField(default=True)
    last_login = fields.DatetimeField(null=True, validators="Был в сети")
    is_superuser = fields.BooleanField(default=False, description="Суперпользователь")
    is_staff = fields.BooleanField(default=False, description="Модератор")
    first_name = fields.CharField(max_length=250, null=True, description="Имя")
    last_name = fields.CharField(max_length=250, null=True, description="Фамилия")
    email = fields.CharField(max_length=256, null=True, description="Почта")
    date_joined = fields.DatetimeField(auto_now_add=True, description="Создан")
    role = fields.CharEnumField(UserRole, max_length=10, default=UserRole.CLIENT, description="Роль пользователя")

    def __str__(self):
        return self.username

    class Meta:
        table = "users_user"


class UserRepo(BaseUserRepo, GenericMixin):
    """
    Репозиторий пользователя
    """
    model = User
