from django.contrib import admin

from gateway.models import Gateway

# Register your models here.
# TODO make sure to add the admin support for gateway app

class GatewayAdmin(admin.ModelAdmin):
    pass

admin.site.register(Gateway, GatewayAdmin)