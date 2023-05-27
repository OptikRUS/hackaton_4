from calendar import monthrange
from datetime import date

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path

from ..models import Slot
from ..fixtures import add_slots


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = (
        "slot_date",
        "time_interval",
        "is_open",
        "supervisor",
    )
    date_hierarchy = "slot_date"
    list_filter = ("is_open", "slot_date", "slot_time", "supervisor")
    list_per_page = 12
    change_list_template = "meetings/slots_changelist.html"

    def time_interval(self, time) -> str:
        return time.get_hour_slot

    time_interval.short_description = "Время слота"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('add_new_month/', self.add_new_month),
            path('remove_month/', self.remove_month),
        ]
        return my_urls + urls

    def add_new_month(self, request) -> HttpResponseRedirect:
        if month := request.POST.get("month"):
            add_slots(month=int(month))
            self.message_user(request, f"Слоты для {month} месяц добавлены")
            return HttpResponseRedirect("../")
        else:
            self.message_user(request, "Вы не ввели месяц")
            return HttpResponseRedirect("../")

    def remove_month(self, request) -> HttpResponseRedirect:
        if month := request.POST.get("month"):
            month: int = int(month)
            today: date = date.today()
            start_of_month: date = date(day=1, month=month, year=today.year)
            _, last_day_of_month = monthrange(today.year, month)
            end_of_month: date = date(day=last_day_of_month, month=month, year=today.year)
            Slot.objects.filter(slot_date__range=(start_of_month, end_of_month)).delete()
            self.message_user(request, f"Слоты для {month} месяца удалены")
            return HttpResponseRedirect("../")
        else:
            self.message_user(request, "Вы не ввели месяц")
            return HttpResponseRedirect("../")
