from django.shortcuts import render
from sad_app.models import Membro
from sad_app.models import Publicacao
from sad_app.models import tipoPublicacao
from sad_app.models import Cargo

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
    
    context = {
        
    }
    
    return render(request, 'contato.html', context)