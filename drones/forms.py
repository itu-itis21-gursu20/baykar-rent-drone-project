from django import forms
from .models import Drone

class DroneForm(forms.ModelForm):
    class Meta:
        model = Drone
        fields = ['brand', 'model', 'weight', 'category']
