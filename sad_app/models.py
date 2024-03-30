from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from django.core.exceptions import ValidationError
    

class Formacao(models.Model):
    class NivelFormacao(models.TextChoices):
        GRADUACAO = 'GR', 'Graduação'
        ESPECIALIZACAO = 'ES', 'Especialização'
        MESTRADO = 'ME', 'Mestrado'
        DOUTORADO = 'DO', 'Doutorado'
        POS_DOUTORADO = 'PD', 'Pós-Doutorado'
        
    class TipoCurso(models.TextChoices):
        BACHARELADO = 'BA', 'Bacharelado'
        LICENCIATURA = 'LI', 'Licenciatura'
        TECNOLOGIA = 'TE', 'Tecnologia'
        POS_GRADUACAO = 'PG', 'Pós-Graduação'
    fk_membro = models.ForeignKey("Membro", on_delete=models.CASCADE)
    instituicao = models.CharField(max_length=100)
    nivel_formacao = models.CharField(max_length=2, choices=NivelFormacao.choices)
    nome_curso = models.CharField(max_length=100)
    modalidade = models.CharField(max_length=2, choices=TipoCurso.choices)
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
    

class Membro(models.Model):
    class Cargo(models.TextChoices):
        ADVOGADO = 'AD', 'Advogado'
        CONSULTOR = 'CO', 'Consultor'
    
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=2, choices=Cargo.choices)
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
    titulo = models.CharField(max_length=50)
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
