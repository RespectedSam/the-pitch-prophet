from django.contrib import admin
from django.urls import path
from prophet.views import landing_page  # Imports your homepage logic

urlpatterns = [
    path('admin/', admin.site.urls),        # Your admin backend panel
    path('', landing_page, name='home'),    # The main Pitch Prophet landing page
]