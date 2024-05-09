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
from .models import Publicacao
from .models import tipoPublicacao
from django.contrib.auth.models import User

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
        widgets = {'email': forms.EmailInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome Completo*', 'required': 'required'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'E-mail*', 'required': 'required'})
        self.fields['assunto'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Assunto*', 'required': 'required'})
        self.fields['mensagem'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Mensagem*', 'required': 'required', 'rows': '4'})

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
        
        
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'fk_instituicao', 'fk_modalidade', 'fk_nivel']
        labels = {
            'nome': 'Nome',
            'fk_instituicao': 'Instituição',
            'fk_modalidade': 'Modalidade',
            'fk_nivel': 'Nível de Formação'
        }
        widgets = {
            'fk_instituicao': forms.Select(),
            'fk_modalidade': forms.Select(),
            'fk_nivel': forms.Select()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})
        
        self.fields['fk_instituicao'].widget.attrs.update({'class': 'form-select', 'placeholder': 'Instituição*', 'required': 'required'})
        self.fields['fk_instituicao'].empty_label = "Selecione instituição*"
        
        self.fields['fk_modalidade'].widget.attrs.update({'class': 'form-select', 'placeholder': 'Modalidade*', 'required': 'required'})
        self.fields['fk_modalidade'].empty_label = "Selecione modalidade*"
        
        self.fields['fk_nivel'].widget.attrs.update({'class': 'form-select', 'placeholder': 'Nível de Formação*', 'required': 'required'})
        self.fields['fk_nivel'].empty_label = "Selecione modalidade*"

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
        widgets ={
            'fk_membro': forms.Select(),
            'fk_curso': forms.Select()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['ano_entrada'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ano de Entrada*', 'required': 'required'})
        self.fields['ano_conclusao'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ano de Conclusão'})
        self.fields['titulo_tese'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Título da Tese'})
        
        self.fields['fk_membro'].widget.attrs.update({'class': 'form-select', 'placeholder': 'Membro*', 'required': 'required'})
        self.fields['fk_membro'].empty_label = 'Selecione o membro*'
        
        self.fields['fk_curso'].widget.attrs.update({'class': 'form-select', 'placeholder': 'Curso*', 'required': 'required'})
        self.fields['fk_curso'].empty_label = 'Selecione o curso*'
        
class NacionalidadeForm(forms.ModelForm):
    class Meta:
        model = Nacionalidade
        fields = ['nome_nacionalidade', 'nome_pais', 'sigla_pais']
        labels = {
            'nome_nacionalidade': 'Nome da Nacionalidade',
            'nome_pais': 'Nome do País',
            'sigla_pais': 'Sigla do País'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome_nacionalidade'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome da Nacionalidade*', 'required': 'required'})
        self.fields['nome_pais'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome do País*', 'required': 'required'})
        self.fields['sigla_pais'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Sigla do País*', 'required': 'required'})

        
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
        fields = ['nome', 'cargo', 'cod_oab', 'fk_nacionalidade',  'data_nascimento', 'img_path', 'socio']
        labels = {
            'nome': 'Nome',
            'cargo': 'Cargo',
            'socio': 'Sócio',
            'cod_oab': 'Código OAB',
            'fk_nacionalidade': 'Nacionalidade',
            'data_nascimento': 'Data de Nascimento',
            'img_path': 'Imagem'
        }
        widgets = {
            'fk_nacionalidade': forms.Select(),
            'cargo': forms.Select(),
            'data_nascimento': forms.DateInput()
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})
        self.fields['cod_oab'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Código OAB'})
        self.fields['img_path'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Imagem'})
        self.fields['socio'].widget.attrs.update({'class': 'form-check-input'})
        
        self.fields['data_nascimento'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Data de Nascimento'})
        
        
        self.fields['cargo'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Cargo*', 'required': 'required'})
        self.fields['cargo'].empty_label = 'Selecione o cargo*'
        
        self.fields['fk_nacionalidade'].widget.attrs.update({'class': 'form-select', 'placeholder': 'Nacionalidade*', 'required': 'required'})
        self.fields['fk_nacionalidade'].empty_label = 'Selecione a Nacionalidade*'
        
        
class PublicacaoForm(forms.ModelForm):
    class Meta:
        model = Publicacao
        fields = ['titulo', 'fk_tipo', 'sinopse', 'data_publicacao', 'img_path', 'pdf_path', 'link']
        labels = {
            'titulo': 'Título',
            'fk_tipo': 'Tipo',
            'sinopse': 'Sinopse',
            'data_publicacao': 'Data de Publicação',
            'img_path': 'Imagem',
            'pdf_path': 'PDF',
            'link': 'Link'
        }
        widgets = {
            'fk_tipo': forms.Select()
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['titulo'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Título*', 'required': 'required'})
        self.fields['sinopse'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Sinopse'})
        self.fields['data_publicacao'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Data de Publicação*', 'required': 'required'})
        self.fields['img_path'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Imagem'})
        self.fields['pdf_path'].widget.attrs.update({'class': 'form-control', 'placeholder': 'PDF'})
        self.fields['link'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Link'})
        
        self.fields['fk_tipo'].widget.attrs.update({'class': 'form-select custom-placeholder', 'placeholder': 'Tipo*', 'required': 'required'})
        self.fields['fk_tipo'].empty_label = 'Selecione o tipo*'
        
class TipoPublicacaoForm(forms.ModelForm):
    class Meta:
        model = tipoPublicacao
        fields = ['nome']
        labels = {
            'nome': 'Nome'
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': 'Usuário',
            'password': 'Senha'
        }
        widgets = {
            'password': forms.PasswordInput()
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Usuário*', 'required': 'required'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Senha*', 'required': 'required'})
        

class CadastroUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'username': 'Usuário',
            'email': 'E-mail',
            'password': 'Senha'
        }
        widgets = {
            'password': forms.PasswordInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Sobrenome'})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Usuário*', 'required': 'required'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Senha*', 'required': 'required'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'E-mail*', 'required': 'required'})
