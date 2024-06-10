from django.urls import path
from . import views

app_name = "blogue"
urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('artigo/<int:artigo_id>/', views.pagina_artigo, name='pagina_artigo'),
    path('artigo/<int:artigo_id>/comentarios/', views.pagina_comentarios, name='pagina_comentarios'),
    path('autor/<int:autor_id>/<int:artigo_id>/', views.pagina_autor, name='pagina_autor'),
    path('autor/<int:autor_id>/', views.pagina_autor_sem_artigo, name='pagina_autor_sem_artigo'),
    path('novo_artigo/', views.novo_artigo_view, name='novo_artigo'),
    path('edita_artigo/<int:artigo_id>/', views.edita_artigo_view, name='edita_artigo'),
    path('apaga_artigo/<int:artigo_id>/', views.apaga_artigo_view, name='apaga_artigo'),
    path('novo_comentario/<int:artigo_id>/', views.novo_comentario_view, name='novo_comentario'),
    path('edita_comentario/<int:comentario_id>/', views.edita_comentario_view, name='edita_comentario'),
    path('apaga_comentario/<int:comentario_id>/', views.apaga_comentario_view, name='apaga_comentario'),
    path('edita_autor/<int:autor_id>/<int:artigo_id>/', views.edita_autor_view, name='edita_autor'),
    path('edita_autor/<int:autor_id>/', views.edita_autor_view_sem_artigo, name='edita_autor_sem_artigo'),
    path('cria_autor/', views.cria_autor_view, name='cria_autor')

]