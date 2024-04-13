from django import forms
from .models import Contato
from .models import NivelFormacao
from .models import Modalidade
from .models import Curso
from .models import Instituicao
from .models import Formacao
from .models import Nacionalidade
from .models import Cargo
from .models import Membro


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'assunto', 'mensagem']
        labels = {
            'nome': 'Nome',
            'email': 'E-mail',
            'assunto': 'Assunto',
            'mensagem': 'Mensagem'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome Completo*', 'required': 'required'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'E-mail*', 'required': 'required'})
        self.fields['assunto'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Assunto*', 'required': 'required'})
        self.fields['mensagem'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Mensagem*', 'required': 'required'})

class NivelFormacaoForm(forms.ModelForm):
    class Meta:
        model = NivelFormacao
        fields = ['nome']
        labels = {
            'nome': 'Nome'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})
        
        
class ModalidadeForm(forms.ModelForm):
    class Meta:
        model = Modalidade
        fields = ['nome']
        labels = {
            'nome': 'Nome'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})
        
        
class Curso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'fk_instituicao', 'fk_modalidade', 'fk_nivel']
        labels = {
            'nome': 'Nome',
            'fk_instituicao': 'Instituição',
            'fk_modalidade': 'Modalidade',
            'fk_nivel': 'Nível de Formação'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})
        self.fields['fk_instituicao'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Instituição*', 'required': 'required'})
        self.fields['fk_modalidade'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Modalidade*', 'required': 'required'})
        self.fields['fk_nivel'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nível de Formação*', 'required': 'required'})


class InstituicaoForm(forms.ModelForm):
    class Meta:
        model = Instituicao
        fields = ['nome', 'sigla']
        labels = {
            'nome': 'Nome',
            'sigla': 'Sigla'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})
        self.fields['sigla'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Sigla*', 'required': 'required'})
        
        

class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = ['fk_membro', 'fk_curso', 'ano_entrada', 'ano_conclusao', 'titulo_tese']
        labels = {
            'fk_membro': 'Membro',
            'fk_curso': 'Curso',
            'ano_entrada': 'Ano de Entrada',
            'ano_conclusao': 'Ano de Conclusão',
            'titulo_tese': 'Título da Tese'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['fk_membro'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Membro*', 'required': 'required'})
        self.fields['fk_curso'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Curso*', 'required': 'required'})
        self.fields['ano_entrada'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ano de Entrada*', 'required': 'required'})
        self.fields['ano_conclusao'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ano de Conclusão*', 'required': 'required'})
        self.fields['titulo_tese'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Título da Tese*', 'required': 'required'})
        
class NacionalidadeForm(forms.ModelForm):
    class Meta:
        model = Nacionalidade
        fields = ['nome_nacionalidade', 'nome_pais', 'sigla_pais']
        labels = {
            'nome_nacionalidade': 'Nome da Nacionalidade',
            'nome_pais': 'Nome do País',
            'sigla_pais': 'Sigla do País'
        }
        
class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['nome']
        labels = {
            'nome': 'Nome'
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})
        
class MembroForm(forms.ModelForm):
    class Meta:
        model = Membro
        fields = ['nome', 'cargo', 'socio', 'cod_oab', 'fk_nacionalidade', 'fk_nacionalidade', 'data_nascimento', 'img_path']
        labels = {
            'nome': 'Nome',
            'cargo': 'Cargo',
            'socio': 'Sócio',
            'cod_oab': 'Código OAB',
            'fk_nacionalidade': 'Nacionalidade',
            'data_nascimento': 'Data de Nascimento',
            'img_path': 'Imagem'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})
        self.fields['cargo'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Cargo*', 'required': 'required'})
        self.fields['socio'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Sócio*', 'required': 'required'})
        self.fields['cod_oab'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Código OAB*', 'required': 'required'})
        self.fields['fk_nacionalidade'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nacionalidade*', 'required': 'required'})
        self.fields['data_nascimento'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Data de Nascimento*', 'required': 'required'})
        self.fields['img_path'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Imagem*', 'required': 'required'})