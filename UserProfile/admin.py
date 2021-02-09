from django.contrib import admin
from .models import *

@admin.register(Profile)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('user','time_zone')

@admin.register(Activity)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('user','start_time','end_time')
