from django import forms
from .models import Banda, Album, Musica

class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = '__all__'
        labels = {
            'nome': 'Nome Banda',
            'genero': 'Gênero',
            'foto': 'Foto',
            'nacionalidade': 'Nacionalidade',
            'anoDeCriacao': 'Ano de Criação (YYYY)',
            'biografia': 'Biografia',
        }
        widgets = {
            'genero': forms.TextInput(attrs={'placeholder': 'Insira o gênero da banda'}),
            'foto': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'anoDeCriacao': forms.TextInput(attrs={'pattern': '\d{4}', 'title': 'Digite um ano válido (YYYY)'}),
            'biografia': forms.Textarea(attrs={'placeholder': 'Insira a biografia da banda'}),
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['titulo', 'ano', 'capa']
        labels = {
            'titulo': 'Título do Álbum',
            'ano': 'Ano de Lançamento (YYYY)',
            'capa': 'Capa do Álbum',
        }
        widgets = {
            'capa': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'ano': forms.TextInput(attrs={'pattern': '\d{4}', 'title': 'Digite um ano válido (YYYY)'}),
        }

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = ['titulo', 'duracao', 'spotify_link','letra']
        labels = {
            'titulo': 'Título da Música',
            'duracao': 'Duração (M:SS)',
            'spotify_link': 'Link do Spotify (opcional)',
            'letra': 'Letra da Musica (opcional)',
        }
        widgets = {
            'duracao': forms.TextInput(attrs={'placeholder': 'M:SS', 'pattern': '[0-9]:[0-5][0-9]', 'title': 'Digite uma duração válida no formato M:SS'}),
            'letra': forms.Textarea(attrs={'placeholder': 'Insira a letra da musica'}),
        }