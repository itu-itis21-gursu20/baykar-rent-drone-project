from django.test import TestCase
from .models import Drone
from django.urls import reverse

class DroneModelTests(TestCase):
    def setUp(self):
        # Setup run before every test method.
        Drone.objects.create(brand="DJI", model="Phantom", weight=1.5, category="Commercial", is_rented=False)

    def test_drone_creation(self):
        """Tests that a drone is added correctly."""
        drone = Drone.objects.get(brand="DJI")
        self.assertEqual(drone.model, "Phantom")
        self.assertFalse(drone.is_rented)
        self.assertEqual(drone.category, "Commercial")
        
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('list_drones'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('list_drones'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'drones/drone_list.html')

