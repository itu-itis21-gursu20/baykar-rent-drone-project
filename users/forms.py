from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Custom user sign-up form inheriting from Django's built-in UserCreationForm
class SignUpForm(UserCreationForm):
    class Meta:
        model = User  # Specifies the model with which this form is associated
        fields = ('username', 'password1', 'password2')  # Fields included in the form

# Custom login form inheriting from Django's built-in AuthenticationForm
class LoginForm(AuthenticationForm):
    class Meta:
        model = User  # Specifies the model with which this form is associated
        fields = ('username', 'password')  # Fields included in the form
