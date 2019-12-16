from django.contrib import admin
from .models import BusStops
# Register your models here.

class BusStopsAdmin(admin.ModelAdmin):
    list_display = ('name','location')

admin.site.register(BusStops, BusStopsAdmin)
