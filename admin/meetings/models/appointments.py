from django.db import models


class Appointment(models.Model):
    """
    Запись на консультирование
    """
    user: int = models.ForeignKey(
        "users.User",
        related_name="inspector",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Клиент",
    )
    slot: int = models.ForeignKey(
        "meetings.Slot", related_name="slots",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Слот",
    )

    def __str__(self):
        return f"Пользователь: {self.user} {self.slot}"

    class Meta:
        managed = False
        db_table = "appointments"
        verbose_name = "Запись на консультирование"
        verbose_name_plural = "Записи на консультирование"
