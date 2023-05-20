from tortoise import fields
from tortoise.models import Model

from common.orm.mixins import GenericMixin
from ..entities import BaseGisServiceRepo


class GisService(Model):
    """
    Модель сервиса ГИС
    """
    id = fields.IntField(pk=True)
    name: str = fields.CharField(max_length=250, unique=True)
    description: str = fields.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        table = "gis_services"


class GisServiceRepo(BaseGisServiceRepo, GenericMixin):
    """
    Репозиторий сервиса ГИС
    """
    model = GisService
