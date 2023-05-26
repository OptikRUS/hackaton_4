from django.contrib import admin

from ..models import Slot
from ..fixtures import add_slots


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ("slot_date", "time_interval", "is_open", "supervisor",)
    date_hierarchy = "slot_date"
    list_filter = ("is_open", "slot_date", "slot_time", "supervisor")

    actions = ['add_new_month_slots']

    def time_interval(self, time) -> str:
        return time.get_hour_slot

    def add_new_month_slots(self, request, queryset=None) -> None:
        if slot := self.model.objects.last():
            month = slot.slot_date.month + 1
            add_slots(month + 1)
        else:
            add_slots(1)

    add_new_month_slots.short_description = 'Добавить слоты на следующий месяц'
