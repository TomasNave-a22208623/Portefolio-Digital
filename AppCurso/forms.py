from django import forms
from .models import Projeto, Disciplina

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'
        labels = {
            'nome': 'Nome do Projeto',
            'descricao': 'Descrição',
            'conceitos_aplicados': 'Conceitos Aplicados',
            'tecnologias_usadas': 'Tecnologias Usadas',
            'imagem': 'Imagem',
            'video_youtube_link': 'Link do vídeo do Youtube',
            'project_link': 'Link do Projeto',
            'linguagens': 'Linguagens de Programação',
            'disciplina': 'Disciplina Associada',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome do projeto'}),
            'descricao': forms.Textarea(attrs={'placeholder': 'Digite a descrição do projeto'}),
            'conceitos_aplicados': forms.Textarea(attrs={'placeholder': 'Liste os conceitos aplicados'}),
            'tecnologias_usadas': forms.Textarea(attrs={'placeholder': 'Liste as tecnologias usadas'}),
            'imagem': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'video_youtube_link': forms.URLInput(attrs={'placeholder': 'Digite o link do vídeo no YouTube'}),
            'project_link': forms.URLInput(attrs={'placeholder': 'Digite o link do projeto'}),
            'linguagens': forms.CheckboxSelectMultiple(),
            'disciplina': forms.Select(),
        }

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'
        labels = {
            'nome': 'Nome da Disciplina',
            'semestre': 'Semestre',
            'ects': 'ECTS',
            'apresentacao': 'Apresentação',
            'programa': 'Programa',
            'curricularIUnitReadableCode': 'Código Curricular',
            'area_cientifica': 'Área Científica',
            'linguagens': 'Linguagens de Programação',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome da disciplina'}),
            'semestre': forms.Select(choices=[(1, '1'), (2, '2')]),
            'ects': forms.NumberInput(attrs={'placeholder': 'Digite o número de ECTS'}),
            'apresentacao': forms.Textarea(attrs={'placeholder': 'Digite a apresentação da disciplina'}),
            'programa': forms.Textarea(attrs={'placeholder': 'Digite o programa da disciplina'}),
            'curricularIUnitReadableCode': forms.TextInput(attrs={'placeholder': 'Digite o código curricular'}),
            'area_cientifica': forms.TextInput(attrs={'placeholder': 'Digite a área científica'}),
            'linguagens': forms.CheckboxSelectMultiple(),
        }