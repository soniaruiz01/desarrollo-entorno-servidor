from django.urls import path, include
from . import views

app_name = 'aplicacion'

urlpatterns = [
    path("aplicacion", views.aplicacion, name = 'aplicacion')
]
    # connect directions web of proyecto with routes in aplicacion