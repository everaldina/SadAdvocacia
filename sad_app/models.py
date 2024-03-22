from django.db import models

# Create your models here.
class Membro(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    socio = models.BooleanField(default=False)
    cod_oab = models.CharField(max_length=30, blank=True, null=True)
    nacionalidade = models.CharField(max_length=50)
    data_nasimento = models.DateField()
    formacao = models.TextField()
    img_path = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        nome_modificado = self.nome.split(' ')[0] + ' ' + self.nome.split(' ')[-1]
        return nome_modificado