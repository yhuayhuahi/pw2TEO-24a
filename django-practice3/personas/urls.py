from django.urls import path
from . import views

# Creamos urls en la aplicacion para conectar al proyecto
urlpatterns = [
    path('', views.myHomeView)
]
