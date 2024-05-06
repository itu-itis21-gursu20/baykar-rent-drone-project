from django.contrib import admin
from django.urls import path , include
from django.views.generic.base import RedirectView

urlpatterns = [
    # Redirect root URL to the login page permanently.
    path('', RedirectView.as_view(url='/users/login/', permanent=True), name='go-to-login'),
    # Include all URL configurations from the 'users' app.
    path('users/', include('users.urls')),
    # Default Django admin interface.
    path('admin/', admin.site.urls),
    # Include all URL configurations from the 'drones' app.
    path('drones/', include('drones.urls')),
]
