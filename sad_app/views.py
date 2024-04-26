from django.shortcuts import render

from sad_app.models import Publicacao, tipoPublicacao, Cargo
from sad_app.forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.
def home(request):
    cargos = Cargo.objects.all()
    equipe_por_cargo = {}
    
    for cargo in cargos:
        equipe_por_cargo[cargo] = cargo.membro_set.all()
        
    for cargo in equipe_por_cargo:
        for membro in equipe_por_cargo[cargo]:
            membro.formacao_ordenadas = membro.formacao_set.all().order_by('ano_entrada')
    
    context = {
        'equipe_por_cargo': equipe_por_cargo
    }

    return render(request, 'index.html', context)

def login(request):
    if request.method == "GET":
        form_login = LoginForm()

        context = {
            'form_login': form_login,
        }

        return render(request, 'login.html', context=context)
    if request.method == "POST":
        user = authenticate(request.POST['username'], request.POST['password'])
        if user:
            auth_login(request, user)
            HttpResponseRedirect(reverse('home'))

def publicacoes(request):    
    tipoLivro = tipoPublicacao.objects.get(nome = 'Livro')
    livros = Publicacao.objects.filter(fk_tipo=tipoLivro.id).order_by('data_publicacao')
    
    tipoArtigo = tipoPublicacao.objects.get(nome = 'Artigo Científico')
    artigos = Publicacao.objects.filter(fk_tipo=tipoArtigo.id).order_by('data_publicacao')
    
    context = {
        'livros': livros,
        'artigos': artigos,
    }
    
    return render(request, 'publicacoes.html', context)

def contato(request):
    form = ContatoForm()

    if request.method == 'POST':
        form = ContatoForm(request.POST)

        if form.is_valid():
            form.save()
            form = ContatoForm()

    context = {
        'form': form,
    }
    
    return render(request, 'contato.html', context)

def formulario_membro(request):
    form_membro = MembroForm()

    context = {
        'form_membro': form_membro,
    }

    return render(request, 'forms/membro.html', context=context)

def formulario_publicacao(request):
    form_publicacao = PublicacaoForm()
    
    context = {
        'form_publicacao': form_publicacao,
    }
    
    return render(request, 'forms/publicacao.html', context)

def formulario_tipoPublicacao(request):
    if request.method == 'POST':
        form_tipo_publicacao = TipoPublicacaoForm(request.POST)
        if form_tipo_publicacao.is_valid():
            form_tipo_publicacao.save()
            return HttpResponseRedirect(reverse('formulario_tipo_publicacao'))
    else: 
        form_tipo_publicacao = TipoPublicacaoForm()
        
            
    form_tipo_publicacao = TipoPublicacaoForm()
    
    context = {
        'form_tipo_publicacao': form_tipo_publicacao,
    }

    return render(request, 'forms/tipo_publicacao.html', context)

def formulario_formacao(request):
    if request.method == 'POST':
        form_formacao = FormacaoForm(request.POST)
        if form_formacao.is_valid():
            form_formacao.save()
            return HttpResponseRedirect(reverse('formulario_formacao'))
    else:
        form_formacao = FormacaoForm()
        

    context = {
        'form_formacao': form_formacao,
    }

    return render(request, 'forms/formacao.html', context=context)

def formulario_nacionalidade(request):
    form_nacionalidade = NacionalidadeForm()

    context = {
        'form_nacionalidade': form_nacionalidade,
    }

    return render(request, 'forms/nacionalidade.html', context)

def formulario_cargo(request):
    form_cargo = CargoForm()

    context = {
        'form_cargo': form_cargo,
    }

    return render(request, 'forms/cargo.html', context)

def formulario_instituicao(request):
    form_instituicao = InstituicaoForm()

    context = {
        'form_instituicao': form_instituicao,
    }

    return render(request, 'forms/instituicao.html', context)

def formulario_curso(request):
    form_curso = CursoForm()

    context = {
        'form_curso': form_curso,
    }

    return render(request, 'forms/curso.html', context)

def formulario_modalidade(request):
    form_modalidade = ModalidadeForm()

    context = {
        'form_modalidade': form_modalidade,
    }

    return render(request, 'forms/modalidade.html', context)

def formulario_nivel_formacao(request):
    form_nivel = NivelFormacaoForm()
    
    context = {
        'form_nivel': form_nivel,
    }

    return render(request, 'forms/nivel.html', context)

def cadastro(request):
    return render(request, 'cadastro.html')