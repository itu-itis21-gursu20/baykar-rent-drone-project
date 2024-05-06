from django.contrib import admin
from .models import Drone, Rental

class DroneAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'weight', 'category', 'is_rented']
    list_filter = ['is_rented', 'category']
    search_fields = ['brand', 'model']

class RentalAdmin(admin.ModelAdmin):
    list_display = ['drone', 'renter', 'start_time', 'end_time']
    list_filter = ['drone', 'renter']
    search_fields = ['drone__brand', 'drone__model', 'renter__username']

admin.site.register(Drone, DroneAdmin)
admin.site.register(Rental, RentalAdmin)

