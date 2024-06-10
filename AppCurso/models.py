from django.db import models


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    competencias = models.TextField()

    def __str__(self):
        return self.nome

class AreaCientifica(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class LinguagemProgramacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    tecnologias_usadas = models.TextField()
    imagem = models.ImageField(upload_to='projetos_Images/', null=True, blank=True)
    video_youtube_link = models.URLField(null=True, blank=True)
    project_link = models.URLField(null=True, blank=True)
    linguagens = models.ManyToManyField(LinguagemProgramacao,null=True, blank=True)
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    apresentacao = models.TextField()
    programa = models.TextField()
    curricularIUnitReadableCode = models.CharField(max_length=50)
    area_cientifica = models.ForeignKey(AreaCientifica, on_delete=models.CASCADE,null=True, blank=True)
    linguagens = models.ManyToManyField(LinguagemProgramacao,null=True, blank=True)

    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length=100)
    disciplinas = models.ManyToManyField(Disciplina, related_name='docentes')

    def __str__(self):
        return self.nome