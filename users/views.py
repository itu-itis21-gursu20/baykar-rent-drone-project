from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import SignUpForm, LoginForm
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally, you can add a message that tells the user the signup was successful
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('/login')  # Redirect users to the login page
        else:
            # If form is not valid, you might want to show some error messages
            messages.error(request, 'Please correct the error below.')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('/drones/drones')  # Kullanıcıyı home sayfasına yönlendir
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if 'confirm_logout' in request.POST:
        logout(request)
        return redirect('/login')
    return render(request, 'logout.html', {})


