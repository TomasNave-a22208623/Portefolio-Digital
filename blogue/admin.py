from django.contrib import admin

from .models import Autor
from .models import Artigo
from .models import Comentario
from .models import Classificacao
from .models import Categoria



class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome' , 'email')
    ordering = ('nome' , 'email')
    search_fields = ('nome' , 'email')

admin.site.register(Autor , AutorAdmin)

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo' , 'autor' , 'data_publicacao')
    ordering = ('data_publicacao' , 'titulo')
    search_fields = ('titulo' , 'autor', 'data_publicacao')
    filter_horizontal = ('categorias',)


admin.site.register(Artigo , ArtigoAdmin)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('autor' , 'data_comentario' , 'artigo' , 'texto')
    ordering = ('data_comentario' , 'autor')
    search_fields = ('artigo' , 'autor', 'data_comentario')


admin.site.register(Comentario , ComentarioAdmin)

class ClassificacaoAdmin(admin.ModelAdmin):
    list_display = ('artigo' , 'autor' , 'valor')
    ordering = ('valor' , 'artigo')
    search_fields = ('artigo' , 'autor', 'valor')


admin.site.register(Classificacao , ClassificacaoAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome' ,)


admin.site.register(Categoria , CategoriaAdmin)


