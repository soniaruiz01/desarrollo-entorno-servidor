from django.urls import path, include

urlpatterns = [
    # ...
    path('aplicacion/', include('aplicacion.urls')),
]
    