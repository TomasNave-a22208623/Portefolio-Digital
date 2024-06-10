from django.shortcuts import render , redirect
from .models import Artigo, Comentario, Autor, Classificacao, Categoria
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from .forms import ArtigoForm, ComentarioForm , AutorForm

def pagina_inicial(request):
    artigos = Artigo.objects.order_by('-data_publicacao')
    userIsEditor = False

    if request.user.is_authenticated:
        userIsEditor =  request.user.groups.filter(name='EditorBlogue').exists() or request.user.is_superuser

    return render(request, 'blogue/pagina_inicial.html', {'artigos': artigos , 'userIsEditor': userIsEditor})

def pagina_artigo(request, artigo_id):
    artigo = Artigo.objects.get(pk=artigo_id)
    userIsEditor = False

    if request.user.is_authenticated:
        userIsEditor = request.user.first_name == artigo.autor.user.first_name or request.user.is_superuser or request.user.groups.filter(name='EditorBlogue').exists()

    comentarios = Comentario.objects.filter(artigo=artigo)
    num_comentarios = comentarios.count()
    categorias = artigo.categorias.all()
    classificacoes = Classificacao.objects.filter(artigo=artigo)
    autor_associado = Autor.objects.filter(artigo=artigo).first()

    total_classificacoes = sum(classificacao.valor for classificacao in classificacoes)
    media_classificacoes = total_classificacoes / len(classificacoes) if classificacoes else None

    return render(request, 'blogue/pagina_artigo.html', {'artigo': artigo, 'comentarios': comentarios, 'num_comentarios': num_comentarios, 'categorias': categorias, 'media_classificacoes': media_classificacoes, 'autor':autor_associado , 'userIsEditor': userIsEditor})

def pagina_comentarios(request, artigo_id):
    artigo = Artigo.objects.get(pk=artigo_id)
    comentarios = Comentario.objects.filter(artigo=artigo)
    userIsEditor = False

    if request.user.is_authenticated:
        userIsEditor =  request.user.groups.filter(name='EditorBlogue').exists() or request.user.is_superuser

    return render(request, 'blogue/pagina_comentarios.html', {'artigo': artigo, 'comentarios': comentarios, 'userIsEditor': userIsEditor})

def pagina_autor_sem_artigo(request, autor_id):
    autor = Autor.objects.get(pk=autor_id)
    userIsEditor = False

    if request.user.is_authenticated:
        userIsEditor =  request.user.groups.filter(name='EditorBlogue').exists() or request.user.is_superuser

    return render(request, 'blogue/pagina_autor.html', {'autor': autor , 'userIsEditor': userIsEditor})


def pagina_autor(request, autor_id, artigo_id):
    autor = Autor.objects.get(pk=autor_id)
    artigo = Artigo.objects.get(pk=artigo_id)
    userIsEditor = False

    if request.user.is_authenticated:
        userIsEditor =  request.user.groups.filter(name='EditorBlogue').exists() or request.user.is_superuser

    return render(request, 'blogue/pagina_autor.html', {'autor': autor, 'artigo': artigo , 'userIsEditor': userIsEditor})



#-----------------------------------------------------(Formularios Artigo)------------------------------------------------------------------


@login_required
def novo_artigo_view(request):
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.autor = request.user.autor
            artigo.save()
            return redirect('blogue:pagina_inicial')
    else:
        form = ArtigoForm()
    return render(request, 'blogue/novo_artigo.html', {'form': form})

@login_required
def edita_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('blogue:pagina_artigo', artigo_id)
    else:
        form = ArtigoForm(instance=artigo)
    return render(request, 'blogue/edita_artigo.html', {'form': form, 'artigo': artigo})

@login_required
def apaga_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    if request.method == 'POST':
        artigo.delete()
        return redirect('blogue:pagina_inicial')
    return render(request, 'blogue/apaga_artigo.html', {'artigo': artigo})


#-----------------------------------------------------(Formularios Comentatio)------------------------------------------------------------------



@login_required
def novo_comentario_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, pk=artigo_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.autor = request.user.autor
            comentario.save()
            return redirect('blogue:pagina_comentarios', artigo_id)
    else:
        form = ComentarioForm()
    return render(request, 'blogue/novo_comentario.html', {'form': form, 'artigo': artigo})

@login_required
def edita_comentario_view(request, comentario_id):
    comentario = get_object_or_404(Comentario, pk=comentario_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('blogue:pagina_comentarios', comentario.artigo.id)
    else:
        form = ComentarioForm(instance=comentario)
    return render(request, 'blogue/edita_comentario.html', {'form': form, 'comentario': comentario})

@login_required
def apaga_comentario_view(request, comentario_id):
    comentario = get_object_or_404(Comentario, pk=comentario_id)
    if request.method == 'POST':
        comentario.delete()
        return redirect('blogue:pagina_comentarios', comentario.artigo.id)
    return render(request, 'blogue/apaga_comentario.html', {'comentario': comentario})



#-----------------------------------------------------(Formularios Autor)------------------------------------------------------------------





@login_required
def cria_autor_view(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            autor = form.save(commit=False)
            autor.user = request.user
            autor.save()
            return redirect('blogue:pagina_inicial')
    else:
        form = AutorForm()
    return render(request, 'blogue/cria_autor.htlm', {'form': form})

@login_required
def edita_autor_view(request, autor_id , artigo_id):
    autor = get_object_or_404(Autor, id=autor_id)
    artigo = get_object_or_404(Artigo , id = artigo_id)
    if request.method == 'POST':
        form = AutorForm(request.POST, request.FILES, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('blogue:pagina_autor', autor_id=autor_id , artigo_id = artigo_id)
    else:
        form = AutorForm(instance=autor)

    return render(request, 'blogue/edita_autor.html', {'form': form , 'autor': autor ,  'artigo': artigo })

@login_required
def edita_autor_view_sem_artigo(request, autor_id ):
    autor = get_object_or_404(Autor, id=autor_id)
    if request.method == 'POST':
        form = AutorForm(request.POST, request.FILES, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('blogue:pagina_autor', autor_id=autor_id )
    else:
        form = AutorForm(instance=autor)

    return render(request, 'blogue/edita_autor.html', {'form': form , 'autor': autor })

