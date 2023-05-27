from tortoise import fields
from tortoise.models import Model

from common.orm.mixins import GenericMixin
from ..entities import BaseMeetingRepo


class Appointment(Model):
    """
    Запись на консультирование
    """
    id = fields.IntField(pk=True)
    user: fields.ForeignKeyNullableRelation = fields.ForeignKeyField(
        "models.User", related_name="client", on_delete=fields.SET_NULL, null=True,
    )
    inspector: fields.ForeignKeyNullableRelation = fields.ForeignKeyField(
        "models.User", related_name="inspector", on_delete=fields.SET_NULL, null=True,
    )
    slot: fields.ForeignKeyNullableRelation = fields.ForeignKeyField(
        "models.Slot", related_name="slots", on_delete=fields.SET_NULL, null=True,
    )
    topic: int = fields.ForeignKeyField("models.Topic", related_name="topic_name")
    start_url: str = fields.CharField(max_length=2048, description="URL начала встречи", null=True)
    join_url: str = fields.CharField(max_length=2048, description="URL для присоединения", null=True)
    status: str = fields.CharField(max_length=50, default="not_approve", description="Статус встречи")  # "waiting"
    is_approved: bool = fields.BooleanField(default=False, description="Подтверждена")

    def __str__(self):
        return f"{self.user} {self.slot}"

    class Meta:
        table = "appointments"


class AppointmentRepo(BaseMeetingRepo, GenericMixin):
    """
    Репозиторий записи на консультирование
    """
    model: Appointment  = Appointment
