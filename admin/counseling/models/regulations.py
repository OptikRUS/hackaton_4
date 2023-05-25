from django.db import models


class Regulation(models.Model):
    """
    Нормативно-правовой акт
    """
    name: str = models.TextField(null=True, verbose_name="Наименование документа")
    supervisor: int = models.ForeignKey(
        "counseling.Supervisor",
        related_name="supervisor_name",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="КНО",
    )
    supervision: int = models.ForeignKey(
        "counseling.Supervision",
        related_name="supervision_type",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Вид наблюдения",
    )
    regulation_type: int = models.ForeignKey(
        "counseling.RegulationType",
        related_name="regulation_type",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Тип нормативно-правового акта",
    )
    created_at = models.DateField(verbose_name="Дата документа")
    publication_date = models.DateField(verbose_name="Дата публикации")

    def __str__(self) -> str:
        return self.text_shorter(self.name)

    def text_shorter(self, text: str, length=5) -> str:
        words: list[str] = text.split()
        if len(words) > length:
            return " ".join(words[:length]) + "..."
        return text

    class Meta:
        managed = False
        db_table = "regulations"
        verbose_name = "Нормативно-правовой акт"
        verbose_name_plural = "Нормативно-правовые акты"
