from django.shortcuts import render, redirect, get_object_or_404
from .models import Drone, Rental
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db import models
from datetime import datetime


# @login_required
def list_drones(request):
    search_query = request.GET.get('search', '')
    if search_query:
        drones = Drone.objects.filter(
            models.Q(brand__icontains=search_query) |
            models.Q(model__icontains=search_query) |
            models.Q(category__icontains=search_query)
        )
    else:
        drones = Drone.objects.all()
    return render(request, 'drones/drone_list.html', {'drones': drones})


# @login_required
def rent_drone(request, drone_id):
    drone = get_object_or_404(Drone, id=drone_id)
    if request.method == 'POST':
        end_date_str = request.POST.get('end_date')
        # Assuming the end_date is submitted in 'YYYY-MM-DD' format
        end_time = datetime.strptime(end_date_str, '%Y-%m-%d')
        end_time = timezone.make_aware(end_time)  # Make the datetime object timezone aware

        rental = Rental(
            drone=drone,
            renter=request.user,
            start_time=timezone.now(),
            end_time=end_time  # Use the user provided end date
        )
        rental.save()
        drone.is_rented = True
        drone.save()
        return redirect('my_rentals')  # Redirect to a page where the user can see their rentals

    return render(request, 'drones/rent_drone.html', {'drone': drone})

# @login_required
def my_rentals(request):
    rentals = Rental.objects.filter(renter=request.user)
    return render(request, 'drones/my_rentals.html', {'rentals': rentals})

# @login_required
def delete_rental(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)
    drone = rental.drone  # Get the associated drone
    if request.method == 'POST':
        rental.delete()  # Delete the rental
        drone.is_rented = False  # Update the drone's rented status
        drone.save()  # Save the drone
        return redirect('my_rentals')  # Redirect to the list of rentals
    # If not a POST request, display a confirmation page
    return render(request, 'drones/delete_rental.html', {'rental': rental})

# @login_required
def update_rental(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)
    if request.method == 'POST':
        # Form işlemleri ve güncelleme mantığı buraya
        rental.start_time = request.POST.get('start_time') or rental.start_time
        rental.end_time = request.POST.get('end_time')
        rental.save()
        return redirect('my_rentals')
    return render(request, 'drones/update_rental.html', {'rental': rental})

