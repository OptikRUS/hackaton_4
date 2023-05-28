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
    supervisor: int = fields.ForeignKeyField(
        "models.Supervisor", on_delete=fields.SET_NULL, null=True, related_name="inspector",
    )

    def __str__(self):
        return self.username

    class Meta:
        table = "users_user"


class UserGroup(Model):
    """
    Группы пользователей
    """
    group_id = fields.IntField()
    user: int = fields.ForeignKeyField("models.User", related_name="user_group")

    def __str__(self):
        return self.user

    class Meta:
        table = "users_user_groups"


class UserPermission(Model):
    """
    Права пользователей
    """
    permission_id = fields.IntField()
    user: int = fields.ForeignKeyField("models.User", related_name="user")

    def __str__(self):
        return self.user

    class Meta:
        table = "users_user_user_permissions"


class UserRepo(BaseUserRepo, GenericMixin):
    """
    Репозиторий пользователя
    """
    model = User
