from datetime import date

from tortoise import fields
from tortoise.models import Model

from common.orm.mixins import GenericMixin
from ..entities import BaseCounselingRepo


class Regulation(Model):
    """
    Нормативно-правовой акт
    """
    id = fields.IntField(pk=True)
    name: str = fields.TextField(null=True, description="Наименование документа")
    supervisor: int = fields.ForeignKeyField(
        "models.Supervisor", related_name="supervisor_name", on_delete=fields.SET_NULL, null=True,
    )
    supervision: int = fields.ForeignKeyField(
        "models.Supervision", related_name="supervision_type", on_delete=fields.SET_NULL, null=True,
    )
    regulation_type: int = fields.ForeignKeyField(
        "models.Supervision", related_name="regulation_type", on_delete=fields.SET_NULL, null=True,
    )
    created_at: date = fields.DateField(description="Дата документа")
    publication_date: date = fields.DateField(description="Дата публикации")

    def __str__(self):
        return self.name.split()[-5]

    class Meta:
        table = "regulations"


class RegulationRepo(BaseCounselingRepo, GenericMixin):
    """
    Репозиторий нормативно-правового акта
    """
    model = Regulation
