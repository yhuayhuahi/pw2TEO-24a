from django.urls import path
from . import views

# Creamos urls en la aplicacion para conectar al proyecto
urlpatterns = [
    path('myhome', views.myHomeView),
    path('test/', views.mySecondView),
    path('forms/', views.myForm),
    # django 4 y 5
    path('anotherAdd/', views.personasAnotherCreateView),
    path('list/<int:myID>/', views.personasShowObject, name='browsing'),
    path('list/', views.personasListView),
    path('list/<int:myID>/delete/', views.personasDeleteView, name='deleting'),
    
    path('', views.PersonaListView.as_view(), name='persona-list'),
    path('<int:pk>/', views.PersonaDetailsView.as_view(), name = 'persona-detail'),
]
