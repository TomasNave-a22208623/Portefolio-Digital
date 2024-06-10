from django.contrib import admin
from .models import Festival, Localizacao, Banda


class FestivalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_inicio', 'data_fim', 'localizacao')
    list_filter = ('data_inicio', 'localizacao')
    search_fields = ('nome', 'localizacao__nome')
    
admin.site.register(Festival, FestivalAdmin)

class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'pais')
    search_fields = ('nome', 'cidade', 'pais')
    
admin.site.register(Localizacao, LocalizacaoAdmin)

class BandaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'genero')
    search_fields = ('nome', 'genero')

admin.site.register(Banda, BandaAdmin)