from django.urls import path
from . import views

# Creamos urls en la aplicacion para conectar al proyecto
urlpatterns = [
    path('myhome', views.myHomeView),
    path('test/', views.mySecondView),
    path('forms/', views.myForm),
    # django 4
    path('anotherAdd/', views.personasAnotherCreateView),
    path('personas/<int:myID>/', views.personasShowObject, name='browsing'),
    path('personas/', views.personasListView),
    path('personas/<int:myID>/delete/', views.personasDeleteView, name='deleting'),
    # django 5
    path('', views.PersonaListView.as_view(), name='persona-list'),

]
