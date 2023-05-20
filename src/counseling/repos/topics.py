from tortoise import fields
from tortoise.models import Model

from common.orm.mixins import GenericMixin
from ..entities import BaseCounselingRepo


class Topic(Model):
    """
    Тема консультирования
    """
    id = fields.IntField(pk=True)
    name: str = fields.TextField(null=True, description="Название темы консультирования")

    def __str__(self):
        return self.name.split()[-5]

    class Meta:
        table = "topics"


class TopicRepo(BaseCounselingRepo, GenericMixin):
    """
    Репозиторий темы консультирования
    """
    model = Topic
