from django.contrib import admin

from buses.models import Buses


class BusesAdmin(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(Buses, BusesAdmin)

