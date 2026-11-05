from django.urls import path, include
from . import views

app_name = 'calendario'

urlpatterns = [
    path('<str:fecha>', views.calendario, name='calendario'),
]