from django.contrib import admin

from clients.models import Clients


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(Clients, ClientAdmin)


