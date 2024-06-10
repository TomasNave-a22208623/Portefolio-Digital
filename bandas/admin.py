from django.contrib import admin
from .models import Banda, Musica, Album


class MusicaInline(admin.TabularInline):
    model = Musica

class AlbumInline(admin.TabularInline):
    model = Album


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano', 'banda')
    ordering = ('titulo', 'ano')
    search_fields = ('titulo', 'ano', 'banda__nome')
    inlines = [MusicaInline]


admin.site.register(Album, AlbumAdmin)


class BandaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'genero', 'anoDeCriacao', 'nacionalidade')
    ordering = ('nome', 'genero', 'anoDeCriacao')
    search_fields = ('nome', 'nacionalidade')
    inlines = [AlbumInline]


admin.site.register(Banda, BandaAdmin)


class MusicaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'duracao', 'album', 'spotify_link')
    ordering = ('titulo', 'duracao')
    search_fields = ('titulo', 'album__titulo')


admin.site.register(Musica, MusicaAdmin)
