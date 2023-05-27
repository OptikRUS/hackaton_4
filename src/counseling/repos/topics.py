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

    def __str__(self) -> str:
        return self.text_shorter(self.name)

    def text_shorter(self, text: str, length=5) -> str:
        words: list[str] = text.split()
        if len(words) > length:
            return " ".join(words[:length]) + "..."
        return text

    class Meta:
        table = "topics"


class TopicRepo(BaseCounselingRepo, GenericMixin):
    """
    Репозиторий темы консультирования
    """
    model = Topic
