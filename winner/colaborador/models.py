from django.db import models
from django.utils import timezone

# Create your models here.
class colaborador(models.Model):
    CG = (
        ('1', 'Diretor'),
        ('2', 'Professor'),
        ('3', 'Recepcionista'),
    )
    id = models.AutoField(primary_key=True)
    cargo = models.CharField(max_length=1, choices=CG)
    nome = models.CharField(max_length=200)
    data_nasc = models.DateTimeField(null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    celular = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome