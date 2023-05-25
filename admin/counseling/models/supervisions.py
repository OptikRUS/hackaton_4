from django.db import models


class Supervision(models.Model):
    """
    Вид контроля (надзора)
    """
    name: str = models.TextField(null=True, verbose_name="Вид контроля (надзора)")
    supervisor: int = models.ForeignKey(
        "counseling.Supervisor",
        related_name="supervisors",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="КНО",
    )

    def __str__(self) -> str:
        return self.text_shorter(self.name)

    def text_shorter(self, text: str, length=5) -> str:
        words: list[str] = text.split()
        if len(words) > length:
            return " ".join(words[:length]) + "..."
        return text

    class Meta:
        managed = False
        db_table = "supervisions"
        verbose_name = "Вид контроля"
        verbose_name_plural = "Виды контроля"
