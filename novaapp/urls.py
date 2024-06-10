from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'DCapp'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('herois/', views.heroes_view, name='herois'),
    path('viloes/', views.viloes_view, name='viloes'),
    
]