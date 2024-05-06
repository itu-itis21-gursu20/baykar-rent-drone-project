from django.urls import path
from .views import list_drones, rent_drone, my_rentals, delete_rental, update_rental

urlpatterns = [
    path('drones/', list_drones, name='list_drones'),
    path('rent/<int:drone_id>/', rent_drone, name='rent_drone'),
    path('my-rentals/', my_rentals, name='my_rentals'),
    path('rentals/update/<int:rental_id>/', update_rental, name='update_rental'),
    path('rentals/delete/<int:rental_id>/', delete_rental, name='delete_rental'),
]
