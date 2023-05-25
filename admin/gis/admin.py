from django.contrib import admin

from .models import GisService


@admin.register(GisService)
class GisServiceAdmin(admin.ModelAdmin):
    pass
