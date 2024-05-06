from django.test import TestCase
from django.urls import reverse
from .models import Drone

# Test class for the Drone model within our application.
class DroneModelTests(TestCase):
    def setUp(self):
        # Set up is called before each test function execution.
        # Here, we are creating a Drone instance to use in tests.
        Drone.objects.create(brand="DJI", model="Phantom", weight=1.5, category="Commercial", is_rented=False)

    def test_drone_creation(self):
        """Test to ensure that a drone is added correctly with given specifications."""
        drone = Drone.objects.get(brand="DJI")
        self.assertEqual(drone.model, "Phantom")  # Test the model field
        self.assertFalse(drone.is_rented)  # Test that is_rented defaults to False
        self.assertEqual(drone.category, "Commercial")  # Test the category field

    def test_view_url_accessible_by_name(self):
        """Test to ensure that the list_drones URL resolves to the correct view function."""
        response = self.client.get(reverse('list_drones'))  # Uses the URL name to fetch the view
        self.assertEqual(response.status_code, 200)  # Check that the response is 200 OK

    def test_view_uses_correct_template(self):
        """Test to ensure the correct template is used to render list_drones view."""
        response = self.client.get(reverse('list_drones'))
        self.assertEqual(response.status_code, 200)  # Ensure the view is accessible
        self.assertTemplateUsed(response, 'drones/drone_list.html')  # Confirm the right template is used
