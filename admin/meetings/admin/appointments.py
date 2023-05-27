from django.contrib import admin

from ..models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "inspector",
        "slot_time",
        "slot_date",
        "topic",
        "status",
        "is_approved",
    )
    readonly_fields = ("start_url", "join_url", )
    list_filter = ("is_approved", "status", )

    def slot_time(self, meet) -> str:
        return meet.slot.get_hour_slot

    def slot_date(self, meet) -> str:
        return meet.slot.slot_date

    slot_time.short_description = "Время слота"
    slot_date.short_description = "Дата слота"
