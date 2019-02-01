from django.db import models
from django.utils import timezone
from aluno.models import aluno
from classe.models import sala_aula, grupo_aula
from colaborador.models import colaborador

# Create your models here.
class presenca(models.Model):
    PR = (
        ('1', 'Sim'),
        ('2', 'Nao'),
    )
    id = models.AutoField(primary_key=True)
    presente = models.CharField(max_length=1, choices=PR, default=2)
    student = models.ForeignKey(aluno, on_delete=models.CASCADE)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome

class aula(models.Model):
    ES = (
        ('1', 'Agendada'),
        ('2', 'Lecionada'),
        ('3', 'Cancelada'),
    )
    UN = (
        ('1', 'Tres Lagoas'),
        ('2', 'Agua Clara'),
        ('3', 'Ribas do Rio Pardo'),
        ('4', 'Campo Grande'),
    )
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=1, choices=ES, default=1)
    unidade = models.CharField(max_length=1, choices=UN, default=1)
    group = models.ForeignKey(grupo_aula, on_delete=models.CASCADE)
    pro = models.ForeignKey(colaborador, on_delete=models.CASCADE)
    classe =models.ForeignKey(sala_aula, on_delete=models.CASCADE)
    presentes = models.ManyToManyField(presenca)
    data_aula = models.DateTimeField(default=timezone.now)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.__str__(id)