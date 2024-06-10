from django.db import models

class Localizacao(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Festival(models.Model):
    nome = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='imagensFestivais/', null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    bandas = models.ManyToManyField(Banda)

    def __str__(self):
        return self.nome