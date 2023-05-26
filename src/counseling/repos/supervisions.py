from tortoise import fields
from tortoise.models import Model

from common.orm.mixins import GenericMixin
from ..entities import BaseCounselingRepo


class Supervision(Model):
    """
    Вид контроля (надзора)
    """
    id = fields.IntField(pk=True)
    name: str = fields.TextField(null=True, description="Вид контроля (надзора)")
    supervisor: int = fields.ForeignKeyField("models.Supervisor", related_name="supervisions")

    def __str__(self):
        return self.name.split()[-5]

    class Meta:
        table = "supervisions"


class SupervisionRepo(BaseCounselingRepo, GenericMixin):
    """
    Репозиторий вида контроля (надзора)
    """
    model = Supervision
