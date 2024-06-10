from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='band_photos/')
    nacionalidade = models.CharField(max_length=100, null=True, blank=True)
    anoDeCriacao = models.IntegerField(null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    ano = models.IntegerField()
    capa = models.ImageField(upload_to='album_covers/')
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, null=True, blank=True, related_name='albuns')

    def __str__(self):
        return f"{self.titulo} - {self.ano}"

class Musica(models.Model):
    titulo = models.CharField(max_length=100)
    duracao = models.CharField(max_length=7)
    spotify_link = models.URLField(blank=True, null=True)
    letra = models.TextField(default='', null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE , null=True, blank=True, related_name='musicas')

    def __str__(self):
        return f"{self.titulo} ({self.duracao})"
