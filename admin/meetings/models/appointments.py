from django.db import models


class Appointment(models.Model):
    """
    Запись на консультирование
    """
    supervisor: int = models.ForeignKey(
        "counseling.Supervisor",
        related_name="appointment",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="КНО",
    )
    user: int = models.ForeignKey(
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

    def __str__(self):
        return f"{self.supervisor} {self.slot}"

    class Meta:
        managed = False
        db_table = "appointments"
        verbose_name = "Запись на консультирование"
        verbose_name_plural = "Записи на консультирование"
