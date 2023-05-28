from django.db import models
from django.utils.translation import gettext_lazy as _


class Appointment(models.Model):
    """
    Запись на консультирование
    """
    class Status(models.TextChoices):
        WAIT = "waiting", _("Ожидание встречи")
        NOT_APPROVE = "not_approve", _("Ожидает подтверждения")
        REJECTED = "rejected", _("Отклонено")

    user: int = models.ForeignKey(
        "users.User",
        related_name="client",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Клиент",
    )
    inspector: int = models.ForeignKey(
        "users.User",
        related_name="inspector",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Инспектор",
    )
    slot: int = models.ForeignKey(
        "meetings.Slot", related_name="slots",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Слот",
    )
    topic: int = models.ForeignKey(
        "counseling.Topic",
        on_delete=models.SET_NULL,
        related_name="topic_name",
        null=True,
        verbose_name="Тема консультации",
    )
    start_url: str = models.CharField(max_length=2048, verbose_name="URL начала встречи")
    join_url: str = models.CharField(max_length=2048, verbose_name="URL для присоединения")
    status = models.CharField(
        choices=Status.choices,
        max_length=50,
        blank=True,
        default=Status.WAIT,
        verbose_name="Статус",
    )
    is_approved: bool = models.BooleanField(default=False, verbose_name="Подтверждена инспектором")

    def __str__(self):
        return f"Пользователь: {self.user} {self.slot}"

    class Meta:
        managed = False
        db_table = "appointments"
        verbose_name = "Запись на консультирование"
        verbose_name_plural = "Записи на консультирование"
