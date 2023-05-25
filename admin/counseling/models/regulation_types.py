from django.db import models


class RegulationType(models.Model):
    """
    Тип нормативно-правового акта
    """
    name: str = models.CharField(max_length=100, null=True, verbose_name="Название типа нормативно-правового акта")

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = "regulation_types"
        verbose_name = "Тип нормативно-правового акта"
        verbose_name_plural = "Типы нормативно-правового акта"
