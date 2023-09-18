from django.contrib import admin
from .models import Fish, FishSpieces


class FishAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'kilme', 'rusis')
    list_filter = ('kilme', 'rusis', 'pavadinimas')

    search_fields = ["id", "fish__kilme", "fish__rusis"]


# Register your models here.
admin.site.register(Fish, FishAdmin)
admin.site.register(FishSpieces)
