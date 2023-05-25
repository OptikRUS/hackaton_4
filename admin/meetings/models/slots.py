from django.db import models


class Slot(models.Model):
    """
    Слот записи на консультирование
    """
    slot_date = models.DateField(verbose_name="Дата слота")
    slot_time = models.TimeField(verbose_name="Время слота")
    is_open: bool = models.BooleanField(verbose_name="Доступность слота", default=True)

    def __str__(self):
        return f"{self.slot_date} {self.slot_time}"

    class Meta:
        managed = False
        db_table = "slots"
        verbose_name = "Слот записи на консультирование"
        verbose_name_plural = "Слоты записей на консультирование"
