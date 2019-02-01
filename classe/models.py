from django.db import models
from django.utils import timezone
from aluno.models import aluno
from colaborador.models import colaborador

# Create your models here.
class sala_aula(models.Model):
    UN = (
        ('1', 'Tres Lagoas'),
        ('2', 'Agua Clara'),
        ('3', 'Ribas do Rio Pardo'),
        ('4', 'Campo Grande'),
    )
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    max_alunos = models.CharField(max_length=20, null=True, blank=True)
    unidade = models.CharField(max_length=1, choices=UN, default=1)
    obs = models.CharField(max_length=400, null=True, blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome

class grupo_aula(models.Model):
    UN = (
        ('1', 'Tres Lagoas'),
        ('2', 'Agua Clara'),
        ('3', 'Ribas do Rio Pardo'),
        ('4', 'Campo Grande'),
    )
    id = models.AutoField(primary_key=True)
    unidade = models.CharField(max_length=1, choices=UN, default=1)
    nome = models.CharField(max_length=200)
    alunos = models.ManyToManyField(aluno)
    livro = models.CharField(max_length=4, null=True, blank=True)
    pag_atual = models.CharField(max_length=4, null=True, blank=True)
    obs = models.CharField(max_length=400, null=True, blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome

