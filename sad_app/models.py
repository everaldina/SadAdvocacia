from django.db import models

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
        return self.nome

class Publicacao(models.Model):
    tipo = models.ForeignKey("tipoPublicacao", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    data_publicacao = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.titulo
    
class tipoPublicacao(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
