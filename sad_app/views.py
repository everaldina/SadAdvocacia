from django.shortcuts import render

from sad_app.models import Membro
from sad_app.models import Publicacao
from sad_app.models import tipoPublicacao
from sad_app.models import Cargo

from sad_app.forms import ContatoForm
from sad_app.forms import PublicacaoForm
from sad_app.forms import TipoPublicacaoForm

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
    return render(request, 'formulario_membro.html')

def formulario_publicacao(request):
    form_publicacao = PublicacaoForm()
    form_tipo_publicacao = TipoPublicacaoForm()
    
    context = {
        'form_publicacao': form_publicacao,
        'form_tipo_publicacao': form_tipo_publicacao,
    }
    return render(request, 'formulario_publicacao.html', context)

def formulario_formacao(request):
    return render(request, 'formulario_formacao.html')