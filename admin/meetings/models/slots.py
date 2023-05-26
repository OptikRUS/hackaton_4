from datetime import time

from django.db import models


class Slot(models.Model):
    """
    Слот записи на консультирование
    """
    slot_date = models.DateField(verbose_name="Дата слота")
    slot_time = models.TimeField(verbose_name="Время слота")
    is_open: bool = models.BooleanField(verbose_name="Доступность слота", default=True)

    def __str__(self):
        return f"Дата: {self.slot_date}\nВремя: {self.get_hour_slot}"

    @property
    def get_hour_slot(self):
        return f"{time(self.slot_time.hour)} – {time(self.slot_time.hour + 1)}"

    class Meta:
        managed = False
        db_table = "slots"
        verbose_name = "Слот записи на консультирование"
        verbose_name_plural = "Слоты записи на консультирование"
