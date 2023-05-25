from django.db import models


class GisService(models.Model):
    """
    Модель сервиса ГИС
    """
    name: str = models.CharField(max_length=250, unique=True)
    description: str = models.TextField(null=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = "gis_services"
        verbose_name = "Сервиса ГИС"
        verbose_name_plural = "Сервисы ГИС"
