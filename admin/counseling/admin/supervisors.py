from django.contrib import admin

from ..models import Supervisor


@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):
    pass
