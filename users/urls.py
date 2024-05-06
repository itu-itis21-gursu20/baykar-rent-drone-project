from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for the login page
    path('login/', views.login, name='login'),
    # URL pattern for the signup page
    path('signup/', views.signup, name='signup'),
    # URL pattern for the logout action
    path('logout/', views.logout_view, name='logout'),
]

