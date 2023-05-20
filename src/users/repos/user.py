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
    role = fields.CharEnumField(UserRole, max_length=10, default=UserRole.CLIENT, description="Роль пользователя")

    def __str__(self):
        return self.username

    class Meta:
        table = "users"


class UserRepo(BaseUserRepo, GenericMixin):
    """
    Репозиторий пользователя
    """
    model = User
