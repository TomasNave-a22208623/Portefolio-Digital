from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('contactos/', views.contactos, name='contactos'),
    path('sobremim/', views.sobre_view, name='sobremim'),
    path('programacaoWeb/', views.programacao_view, name='programacaoWeb'),

]