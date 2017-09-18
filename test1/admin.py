from django.contrib import admin
from .models import (StationModel)
# Register your models here.

class StationAdmin(admin.ModelAdmin):
	list_display = ['station_name','created_at']



admin.site.register(StationModel, StationAdmin)