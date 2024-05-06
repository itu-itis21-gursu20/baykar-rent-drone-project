from django.contrib import admin
from .models import Drone, Rental

# Admin interface customization for the Drone model
class DroneAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the admin list view
    list_display = ['brand', 'model', 'weight', 'category', 'is_rented']
    # Enable filters for these fields in the admin interface
    list_filter = ['is_rented', 'category']
    # Allow searching by brand and model in the admin interface
    search_fields = ['brand', 'model']

# Admin interface customization for the Rental model
class RentalAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the admin list view
    list_display = ['drone', 'renter', 'start_time', 'end_time']
    # Enable filters by drone and renter in the admin interface
    list_filter = ['drone', 'renter']
    # Allow searching by drone brand/model and renter username
    search_fields = ['drone__brand', 'drone__model', 'renter__username']

# Registering the Drone and Rental models with their respective admin class
admin.site.register(Drone, DroneAdmin)
admin.site.register(Rental, RentalAdmin)

