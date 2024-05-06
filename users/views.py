from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import SignUpForm, LoginForm
from django.contrib import messages

# View for handling user sign-up
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():  # Check if form data is valid
            user = form.save()  # Save the new user to the database
            # Display a success message
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('/login')  # Redirect to the login page after successful signup
        else:
            # Display an error message if form is not valid
            messages.error(request, 'Please correct the error below.')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})  # Render the signup page with the form

# View for handling user login
def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():  # Check if form data is valid
            user = form.get_user()
            auth_login(request, user)  # Log the user in
            return redirect('/drones/drones')  # Redirect to a drones listing page
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})  # Render the login page with the form

# View for handling user logout
def logout_view(request):
    if 'confirm_logout' in request.POST:
        logout(request)  # Log the user out
        return redirect('/login')  # Redirect to the login page after logout
    return render(request, 'logout.html', {})  # Render the logout confirmation page


