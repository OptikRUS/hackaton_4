from django.db import models


class Consultation(models.Model):
    """
    Консультация
    """
    name: str = models.TextField(null=True, verbose_name="Тема консультирования")
    supervisor: int = models.ForeignKey(
        "counseling.Supervisor",
        related_name="supervisor",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="КНО",
    )
    supervision: int = models.ForeignKey(
        "counseling.Supervision",
        related_name="supervision",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Вид наблюдения",
    )
    topic: int = models.ForeignKey(
        "counseling.Topic",
        related_name="topic",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Тема консультирования",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        managed = False
        db_table = "consultations"
        verbose_name = "Консультация"
        verbose_name_plural = "Консультации"
