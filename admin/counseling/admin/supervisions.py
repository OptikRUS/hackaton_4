from django.contrib import admin

from ..models import Supervision


@admin.register(Supervision)
class SupervisionAdmin(admin.ModelAdmin):
    pass
