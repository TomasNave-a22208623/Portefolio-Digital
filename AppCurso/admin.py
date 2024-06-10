from django.contrib import admin
from django.utils.html import format_html
from .models import Curso
from .models import AreaCientifica
from .models import LinguagemProgramacao
from .models import Disciplina
from .models import Docente
from .models import Projeto



class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome','apresentacao','objetivos','competencias')


admin.site.register(Curso , CursoAdmin)


class AreaCientificaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

admin.site.register(AreaCientifica , AreaCientificaAdmin)


class LinguagemProgramacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

admin.site.register(LinguagemProgramacao , LinguagemProgramacaoAdmin)


class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre','ects','area_cientifica')
    ordering = ('nome', 'ano', 'semestre','ects')
    search_fields = ('nome','ano')
    filter_horizontal = ('linguagens',)



admin.site.register(Disciplina , DisciplinaAdmin)



class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    filter_horizontal = ('disciplinas',)

admin.site.register(Docente , DocenteAdmin)


class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'tecnologias_usadas')
    filter_horizontal = ('linguagens',)
    search_fields = ('nome',)

admin.site.register(Projeto , ProjetoAdmin)