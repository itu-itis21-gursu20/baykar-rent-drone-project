from django.db import models
from django.contrib.auth.models import User

# Model definition for Drone
class Drone(models.Model):
    brand = models.CharField(max_length=100, verbose_name="Marka")
    model = models.CharField(max_length=100, verbose_name="Model")
    weight = models.FloatField(verbose_name="Ağırlık")
    category = models.CharField(max_length=100, verbose_name="Kategori")
    is_rented = models.BooleanField(default=False, verbose_name="Kirada mı")

    # String representation of a Drone object
    def __str__(self):
        return f"{self.brand} {self.model}"

# Model definition for Rental
class Rental(models.Model):
    drone = models.ForeignKey('Drone', on_delete=models.CASCADE, related_name='rentals')
    renter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rentals')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    # String representation of a Rental object
    def __str__(self):
        return f"{self.drone} rented by {self.renter}"
