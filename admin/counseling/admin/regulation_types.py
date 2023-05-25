from django.contrib import admin

from ..models import RegulationType


@admin.register(RegulationType)
class RegulationTypeAdmin(admin.ModelAdmin):
    pass
