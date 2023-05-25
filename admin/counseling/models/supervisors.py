from django.db import models


class Supervisor(models.Model):
    """
    Модель Контрольно-надзорного органа (КНО)
    """
    name: str = models.TextField(null=True, verbose_name="Наименование контрольного (надзорного) органа")

    def __str__(self) -> str:
        return self.text_shorter(self.name)

    def text_shorter(self, text: str, length=5) -> str:
        words: list[str] = text.split()
        if len(words) > length:
            return " ".join(words[:length]) + "..."
        return text

    class Meta:
        managed = False
        db_table = "supervisors"
        verbose_name = "контрольно-надзорного органа"
        verbose_name_plural = "КНО"
