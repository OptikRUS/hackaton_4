from tortoise import fields
from tortoise.models import Model

from common.orm.mixins import GenericMixin
from ..entities import BaseCounselingRepo


class Consultation(Model):
    """
    Консультация
    """
    id = fields.IntField(pk=True)
    name: str = fields.TextField(null=True, description="Тема консультирования")
    supervisor: int = fields.ForeignKeyField("models.Supervisor", related_name="supervisor")
    supervision: int = fields.ForeignKeyField("models.Supervision", related_name="supervision")
    topic: int = fields.ForeignKeyField("models.Topic", related_name="topic")

    def __str__(self):
        return self.name.split()[-5]

    class Meta:
        table = "consultations"


class ConsultationRepo(BaseCounselingRepo, GenericMixin):
    """
    Репозиторий консультации
    """
    model = Consultation
