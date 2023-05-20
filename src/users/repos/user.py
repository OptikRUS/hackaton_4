from tortoise import fields
from tortoise.models import Model

from common.orm import QBuilder, AnnotationBuilder
from common.orm.mixins import GenericMixin
from common.models import TimeBasedMixin
from ..entities import BaseUserRepo


class User(Model, TimeBasedMixin):
    """
    Модель пользователя
    """

    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(max_length=128, null=True)
    is_active = fields.BooleanField(default=True)
    role = fields.CharField(default='client', max_length=9)

    def __str__(self):
        return self.username

    class PydanticMeta:
        computed = ["username"]
        exclude = ["password"]

    class Meta:
        table = "users"


class UserRepo(BaseUserRepo, GenericMixin):
    """
    Репозиторий пользователя
    """
    model = User
    q_builder: QBuilder = QBuilder(User)
    a_builder: AnnotationBuilder = AnnotationBuilder(User)
