from tortoise import fields
from tortoise.models import Model

from common.orm.mixins import GenericMixin
from ..entities import BaseCounselingRepo


class RegulationType(Model):
    """
    Тип нормативно-правового акта
    """
    id = fields.IntField(pk=True)
    name: str = fields.CharField(max_length=100, null=True, description="Название типа нормативно-правового акта")

    def __str__(self):
        return self.name

    class Meta:
        table = "regulation_types"


class RegulationTypeRepo(BaseCounselingRepo, GenericMixin):
    """
    Репозиторий типа нормативно-правового акта
    """
    model = RegulationType
