from django.urls import path
from .views import list_drones, rent_drone, my_rentals, delete_rental, update_rental

urlpatterns = [
    # URL pattern for listing all drones
    path('drones/', list_drones, name='list_drones'),
    # URL pattern for renting a drone based on drone_id
    path('rent/<int:drone_id>/', rent_drone, name='rent_drone'),
    # URL pattern for viewing a user's current and past rentals
    path('my-rentals/', my_rentals, name='my_rentals'),
    # URL pattern for updating a rental based on rental_id
    path('rentals/update/<int:rental_id>/', update_rental, name='update_rental'),
    # URL pattern for deleting a rental based on rental_id
    path('rentals/delete/<int:rental_id>/', delete_rental, name='delete_rental'),
]

