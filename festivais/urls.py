from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_festivais, name='lista_festivais'),
    path('festival/<int:festival_id>/', views.festival, name='festival'),
]