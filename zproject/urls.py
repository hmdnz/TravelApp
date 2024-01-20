# zproject/urls.py
from django.contrib import admin
from django.urls import path, include
import calc  # Make sure the import is correct based on your project structure

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calc.urls')),  # Use the correct app name in the include statement
]
