
# This file defines the URL route for the sonia_server application

"""
URL configuration for the sonia_server application.
"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
]
