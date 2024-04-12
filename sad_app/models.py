from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from django.core.exceptions import ValidationError


class NivelFormacao(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class Modalidade(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    fk_instituicao = models.ForeignKey("Instituicao", on_delete=models.CASCADE)
    fk_modalidade = models.ForeignKey("Modalidade", on_delete=models.CASCADE)
    fk_nivel = models.ForeignKey("NivelFormacao", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nome} - {self.fk_modalidade} ({self.fk_instituicao.sigla})"

class Instituicao(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nome

class Formacao(models.Model):
    fk_membro = models.ForeignKey("Membro", on_delete=models.CASCADE)
    fk_curso = models.ForeignKey("Curso", on_delete=models.CASCADE, blank=True, null=True)
    ano_entrada = models.IntegerField(validators=[MinValueValidator(1900)])
    ano_conclusao = models.IntegerField(validators=[MaxValueValidator(datetime.datetime.now().year + 4)], blank=True, null=True)
    titulo_tese = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.fk_membro.nome
    
    
    def _validate_ano_conclusao(self):
        if self.ano_conclusao and self.ano_conclusao <= self.ano_entrada:
            raise ValidationError("Ano de conclusão deve ser maior que o ano de entrada.")
    
    def save(self, *args, **kwargs):
        self._validate_ano_conclusao()
        return super().save(*args, **kwargs)

    
    
class Nacionalidade(models.Model):
    nome_nacionalidade = models.CharField(max_length=50)
    nome_pais = models.CharField(max_length=50)
    sigla_pais = models.CharField(max_length=3)
    
    def __str__(self):
        return self.nome_nacionalidade


class Cargo(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome    

class Membro(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    socio = models.BooleanField(default=False)
    cod_oab = models.CharField(max_length=30, blank=True, null=True)
    fk_nacionalidade = models.ForeignKey("Nacionalidade", on_delete=models.PROTECT)
    data_nascimento = models.DateField(blank=True, null=True)
    img_path = models.CharField(max_length=100, blank=True, null=True)
    

    def __str__(self):
        return self.nome
    
    @property
    def nome_modificado(self):
        return self.nome.split(' ')[0] + ' ' + self.nome.split(' ')[-1]

class Publicacao(models.Model):
    fk_tipo = models.ForeignKey("tipoPublicacao", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_publicacao = models.DateField(auto_now=False, auto_now_add=False)
    img_path = models.CharField(max_length=100, blank=True, null=True)
    pdf_path = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=150, blank=True, null=True)
    
    def __str__(self):
        return self.titulo
    
class tipoPublicacao(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
