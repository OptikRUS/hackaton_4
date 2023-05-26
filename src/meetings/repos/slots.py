from datetime import date, time

from tortoise import fields
from tortoise.models import Model

from common.orm.mixins import GenericMixin
from ..entities import BaseMeetingRepo


class Slot(Model):
    """
    Слот записи на консультирование
    """
    id = fields.IntField(pk=True)
    slot_date: date = fields.DateField(description="Дата слота")
    slot_time: time = fields.TimeField(description="Время слота")
    is_open: bool = fields.BooleanField(description="Доступность слота", default=True)
    supervisor: int = fields.ForeignKeyField("models.Supervisor", related_name="slots")

    def __str__(self):
        return f"{self.slot_date} {self.slot_time}"

    class Meta:
        table = "slots"


class SlotRepo(BaseMeetingRepo, GenericMixin):
    """
    Репозиторий слотов
    """
    model: Slot = Slot
