from django.urls import path
from . import views

app_name = "meteo"
urlpatterns = [
    path('tempo_lisboa/', views.tempo_lisboa , name='tempo_lisboa'),
    path('previsao5Dias/', views.previsao_proximos_5_dias, name='previsao_proximos_5_dias'),
    path('inicio/', views.inicio_view , name='inicio'),
    path('api/cidades', views.listar_cidades , name='cidadesAPI'),
    path('api/previsao_hoje/<int:cidade_id>/', views.previsao_hojeAPI , name='previsao_hojeAPI'),
    path('api/previsao_proximos_5_dias/<int:cidade_id>/', views.previsao_proximos_5_diasAPI , name='previsao_proximos_5_diasAPI'),
]