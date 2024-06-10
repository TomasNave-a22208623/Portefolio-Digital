from django.urls import path
from . import views

app_name = "curso"
urlpatterns = [
    path('', views.pagina_curso, name='pagina_curso'),
    path('projetos/', views.pagina_listaprojetos, name='pagina_listaProjetos'),
    path('ano/<int:ano>/', views.pagina_ano, name='pagina_ano'),
    path('disciplina/<int:disciplina_id>/', views.pagina_disciplina, name='pagina_disciplina'),
    path('projeto/<int:projeto_id>/', views.pagina_projeto, name='pagina_projeto'),

    # projetos formularios
    path('novo_projeto/', views.novo_projeto, name='novo_projeto'),
    path('edita_projeto/<int:projeto_id>/', views.editar_projeto, name='edita_projeto'),
    path('apaga_projeto/<int:projeto_id>/', views.apagar_projeto, name='apaga_projeto'),

    # disciplinas formularios
    path('nova_disciplina/<int:ano>/', views.nova_disciplina_view, name='nova_disciplina'),
    path('edita_disciplina/<int:disciplina_id>/', views.edita_disciplina, name='edita_disciplina'),
    path('apaga_disciplina/<int:disciplina_id>/', views.apaga_disciplina, name='apaga_disciplina'),
]
