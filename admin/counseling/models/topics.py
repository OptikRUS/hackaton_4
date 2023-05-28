from django.db import models


class Topic(models.Model):
    """
    Тема консультирования
    """
    name: str = models.TextField(null=True, verbose_name="Название темы консультирования")

    def __str__(self) -> str:
        return self.text_shorter(self.name) if self.name else self.id

    def text_shorter(self, text: str, length=5) -> str:
        words: list[str] = text.split()
        if len(words) > length:
            return " ".join(words[:length]) + "..."
        return text

    class Meta:
        managed = False
        db_table = "topics"
        verbose_name = "Тема консультирования"
        verbose_name_plural = "Темы консультирования"
