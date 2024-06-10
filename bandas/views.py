from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import Banda
from .models import Musica
from .models import Album

from .forms import BandaForm, AlbumForm , MusicaForm



# Create your views here.

def index_view(request):
    userIsEditor = request.user.groups.filter(name='EditorBandas').exists() or request.user.is_superuser

    bandas = Banda.objects.all().order_by('nome')
    context = {
        'bandas': bandas,
        'userIsEditor': userIsEditor,
    }
    return render(request, 'bandas/lista_bandas.html', context)

def banda_view(request, banda_id):
    userIsEditor = request.user.groups.filter(name='EditorBandas').exists() or request.user.is_superuser

    banda = Banda.objects.get(id=banda_id)
    albuns = banda.albuns.all()
    context = {
        'banda': banda,
        'albuns': albuns,
        'userIsEditor': userIsEditor,
    }
    return render(request, 'bandas/banda.html', context)

def album_view(request, album_id):
    userIsEditor = request.user.groups.filter(name='EditorBandas').exists() or request.user.is_superuser

    album = Album.objects.get(id=album_id)
    musicas = album.musicas.all()
    context = {
        'album': album,
        'musicas': musicas,
        'userIsEditor': userIsEditor,
    }
    return render(request, 'bandas/album.html', context)

def musica_view(request, musica_id):
    userIsEditor = request.user.groups.filter(name='EditorBandas').exists() or request.user.is_superuser

    musica = Musica.objects.get(id=musica_id)
    context = {
        'musica': musica,
        'userIsEditor': userIsEditor,
    }
    return render(request, 'bandas/musica.html', context)

def html5_view(request):
    return render(request, 'bandas/htlm5.html')

#-----------------------------------------------------------(Bandas Formularios)----------------------------------------------------------


@login_required
def nova_banda_view(request):
    if request.method == 'POST':
        form = BandaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BandaForm()
    return render(request, 'bandas/nova_banda.html', {'form': form})


@login_required
def edita_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    if request.method == 'POST':
        form = BandaForm(request.POST, request.FILES, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('banda', banda_id)
    else:
        form = BandaForm(instance=banda)
    return render(request, 'bandas/edita_banda.html', {'form': form , 'banda':banda})

@login_required
def apaga_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    if request.method == 'POST':
        banda.delete()
        return redirect('index')

    return render(request, 'bandas/apaga_banda.html', {'banda': banda})


#-----------------------------------------------------------(Albuns Formularios)----------------------------------------------------------


@login_required
def novo_album_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save()
            album.banda = banda
            album.save()
            return redirect('banda', banda_id=banda_id)
    else:
        form = AlbumForm()
    return render(request, 'bandas/novo_album.html', {'form': form, 'banda': banda})


@login_required
def edita_album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album', album_id)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'bandas/edita_album.html', {'form': form, 'album': album})


@login_required
def apaga_album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    banda_id = album.banda.id
    if request.method == 'POST':
        album.delete()
        return redirect('banda', banda_id=banda_id)
    return render(request, 'bandas/apaga_album.html', {'album': album})


#-----------------------------------------------------------(Musicas Formularios)----------------------------------------------------------



@login_required
def nova_musica_view(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.method == 'POST':
        form = MusicaForm(request.POST)
        if form.is_valid():
            musica = form.save()
            musica.album = album
            musica.save()
            return redirect('album', album_id=album_id)
    else:
        form = MusicaForm()
    return render(request, 'bandas/nova_musica.html', {'form': form, 'album': album})

@login_required
def edita_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    if request.method == 'POST':
        form = MusicaForm(request.POST, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('musica', musica_id)
    else:
        form = MusicaForm(instance=musica)
    return render(request, 'bandas/edita_musica.html', {'form': form, 'musica': musica})

@login_required
def apaga_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    album_id = musica.album.id
    if request.method == 'POST':
        musica.delete()
        return redirect('album', album_id=album_id)
    return render(request, 'bandas/apaga_musica.html', {'musica': musica})