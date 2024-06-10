from django.shortcuts import render
from .models import Curso, Disciplina, Projeto
from django.shortcuts import render, redirect
from .forms import ProjetoForm, DisciplinaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

def pagina_inicial(request):
    curso = Curso.objects.first()
    return render(request, 'AppCurso/pagina_inicial.html', {'curso': curso})

def pagina_curso(request):
    curso = Curso.objects.first()
    return render(request, 'AppCurso/pagina_curso.html', {'curso': curso})

def pagina_ano(request, ano):
    userIsEditor = request.user.groups.filter(name='EditorCurso').exists() or request.user.is_superuser
    disciplinas_primeiro_semestre = Disciplina.objects.filter(ano=ano, semestre=1)
    disciplinas_segundo_semestre = Disciplina.objects.filter(ano=ano, semestre=2)
    return render(request, 'AppCurso/pagina_ano.html', {'disciplinas_primeiro_semestre': disciplinas_primeiro_semestre,
                                                'disciplinas_segundo_semestre': disciplinas_segundo_semestre,
                                                'ano': ano , 'userIsEditor': userIsEditor})

def pagina_listaprojetos(request):
    userIsEditor = request.user.groups.filter(name='EditorCurso').exists() or request.user.is_superuser
    projetos_com_disciplina = Projeto.objects.filter(disciplina__isnull=False)
    return render(request, 'AppCurso/pagina_listaProjetos.html', {'projetos': projetos_com_disciplina , 'userIsEditor': userIsEditor})

def pagina_disciplina(request, disciplina_id):
    userIsEditor = request.user.groups.filter(name='EditorCurso').exists() or request.user.is_superuser
    disciplina = Disciplina.objects.get(pk=disciplina_id)
    projeto_associado = Projeto.objects.filter(disciplina=disciplina).first()
    return render(request, 'AppCurso/pagina_disciplina.html', {'disciplina': disciplina, 'projeto_associado': projeto_associado , 'userIsEditor': userIsEditor})

def pagina_projeto(request, projeto_id):
    userIsEditor = request.user.groups.filter(name='EditorCurso').exists() or request.user.is_superuser
    projeto = Projeto.objects.get(pk=projeto_id)
    return render(request, 'AppCurso/pagina_projeto.html', {'projeto': projeto , 'userIsEditor': userIsEditor})



#----------------------------------------------------------(Formularios Projeto)------------------------------------------------------------

@login_required
def novo_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('curso:pagina_listaProjetos')
    else:
        form = ProjetoForm()
    return render(request, 'AppCurso/novo_projeto.html', {'form': form})

@login_required
def editar_projeto(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('curso:pagina_projeto', projeto_id=projeto_id)
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'AppCurso/editar_projeto.html', {'form': form, 'projeto': projeto})

@login_required
def apagar_projeto(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('curso:pagina_listaProjetos')
    return render(request, 'AppCurso/apagar_projeto.html', {'projeto': projeto})




#----------------------------------------------------------(Formularios Projeto)------------------------------------------------------------


@login_required


def nova_disciplina_view(request, ano):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            disciplina = form.save(commit=False)
            disciplina.ano = ano  # Definindo o ano da disciplina com base no parâmetro da URL
            disciplina.save()
            return redirect('curso:pagina_ano', ano=ano)
    else:
        form = DisciplinaForm(initial={'ano': ano})  # Define o valor inicial do campo 'ano'
    return render(request, 'AppCurso/nova_disciplina.html', {'form': form , 'ano': ano })

@login_required
def edita_disciplina(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('curso:pagina_disciplina', disciplina_id=disciplina_id)
    else:
        form = DisciplinaForm(instance=disciplina)
    return render(request, 'AppCurso/editar_disciplina.html', {'form': form, 'disciplina': disciplina})

@login_required
def apaga_disciplina(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    if request.method == 'POST':
        disciplina.delete()
        return redirect('curso:pagina_inicial')  # ou para qualquer outra página
    return render(request, 'AppCurso/apagar_disciplina.html', {'disciplina': disciplina})
