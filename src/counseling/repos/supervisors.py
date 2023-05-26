from tortoise import fields
from tortoise.models import Model

from common.orm.mixins import ReadWriteMixin
from ..entities import BaseCounselingRepo


class Supervisor(Model):
    """
    Модель Контрольно-надзорного органа (КНО)
    """
    id = fields.IntField(pk=True)
    name: str = fields.TextField(null=True, description="Наименование контрольного (надзорного) органа")
    supervisions: list['Supervision']

    def __str__(self):
        return self.name.split()[-5]

    class Meta:
        table = "supervisors"


class SupervisorRepo(BaseCounselingRepo, ReadWriteMixin):
    """
    Репозиторий КНО
    """
    model: Supervisor = Supervisor
