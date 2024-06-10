from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    biografia = models.TextField()
    imagem = models.ImageField(upload_to='autores_imagens/', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'autor')

    def __str__(self):
        return self.nome

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='artigo_imagens/', blank=True, null=True)
    categorias = models.ManyToManyField('Categoria', related_name= 'categorias')

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios', blank=True, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE,  blank=True, null=True)
    texto = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)



class Classificacao(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='classificacoes')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    VALOR_CHOICES=[
            (1 , "1"),
            (2 , "1.5"),
            (3 , "2"),
            (4 , "2.5"),
            (5 , "3"),
            (6 , "3.5"),
            (7 , "4"),
            (8 , "4.5"),
            (9 , "5"),
    ]

    valor = models.IntegerField(choices=VALOR_CHOICES,default=1)




class Categoria(models.Model):
    nome = models.CharField(max_length = 100)


    def __str__(self):
        return self.nome



