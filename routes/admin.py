from django.contrib import admin

from routes.models import Stations, Costs, Routes


class StationsAdmin(admin.ModelAdmin):
    list_display = ('id',)


class CostsAdmin(admin.ModelAdmin):
    list_display = ('id',)


class RoutesAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(Stations, StationsAdmin)
admin.site.register(Costs, CostsAdmin)
admin.site.register(Routes, RoutesAdmin)


