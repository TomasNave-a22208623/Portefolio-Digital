from django import forms
from .models import Artigo, Comentario, Autor

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['titulo', 'conteudo', 'imagem', 'categorias']
        labels = {
            'titulo': 'Título do Artigo',
            'conteudo': 'Conteúdo',
            'imagem': 'Imagem do Artigo',
            'categorias': 'Categorias',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Digite o título do artigo'}),
            'conteudo': forms.Textarea(attrs={'placeholder': 'Digite o conteúdo do artigo'}),
            'imagem': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'categorias': forms.CheckboxSelectMultiple(),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        labels = {
            'texto': 'Texto do Comentário',
        }
        widgets = {
            'texto': forms.Textarea(attrs={'placeholder': 'Digite seu comentário'}),
        }

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'biografia', 'email', 'imagem']
        labels = {
            'nome': 'Nome do Autor',
            'biografia': 'Biografia',
            'email': 'E-mail',
            'imagem': 'Imagem do Autor',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome do autor'}),
            'biografia': forms.Textarea(attrs={'placeholder': 'Digite a biografia do autor'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Digite o e-mail do autor'}),
            'imagem': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }