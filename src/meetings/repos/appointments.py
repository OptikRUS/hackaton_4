from tortoise import fields
from tortoise.models import Model

from common.orm.mixins import GenericMixin
from ..entities import BaseMeetingRepo


class Appointment(Model):
    """
    Запись на консультирование
    """
    id = fields.IntField(pk=True)
    supervisor: int = fields.ForeignKeyField(
        "models.Supervisor", related_name="appointment", on_delete=fields.SET_NULL, null=True,
    )
    user: int = fields.ForeignKeyField(
        "models.User", related_name="inspector", on_delete=fields.SET_NULL, null=True,
    )
    slot: int = fields.ForeignKeyField(
        "models.Slot", related_name="slots", on_delete=fields.SET_NULL, null=True,
    )

    def __str__(self):
        return f"{self.supervisor} {self.slot}"

    class Meta:
        table = "appointments"


class AppointmentRepo(BaseMeetingRepo, GenericMixin):
    """
    Репозиторий записи на консультирование
    """
    model = Appointment
