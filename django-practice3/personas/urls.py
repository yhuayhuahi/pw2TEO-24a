from django.urls import path
from . import views

# Creamos urls en la aplicacion para conectar al proyecto
urlpatterns = [
    path('', views.myHomeView),
    path('test/', views.mySecondView),
    path('forms/', views.myForm),
    # django 4 y 5
    path('anotherAdd/', views.personasAnotherCreateView)
]
