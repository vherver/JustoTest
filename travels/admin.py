from django.contrib import admin

from travels.models import Travel, TravelClients


class TravelAdmin(admin.ModelAdmin):
    list_display = ('id',)


class TravelClientsAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(Travel, TravelAdmin)
admin.site.register(TravelClients, TravelClientsAdmin)
