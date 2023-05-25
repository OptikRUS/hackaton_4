from django.contrib import admin

from ..models import Regulation


@admin.register(Regulation)
class RegulationAdmin(admin.ModelAdmin):
    pass
