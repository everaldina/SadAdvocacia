from django.shortcuts import render
from sad_app.models import Membro
from sad_app.models import Publicacao
from sad_app.models import tipoPublicacao

# Create your views here.
def home(request):
    equipe = Membro.objects.order_by('id')
    consultor = []
    advogado = []
    for e in equipe:
        if e.cargo == 'Consultor':
            consultor.append(e)
        else:
            advogado.append(e)
    context = {
        'consultores': consultor,
        'advogados': advogado,
    }
    return render(request, 'index.html', context)

def publicacoes(request):
    publicacoes = Publicacao.objects.order_by('data_publicacao')
    
    context = {
        'publicacoes': publicacoes,
    }
    
    return render(request, 'publicacoes.html', context)


def contato(request):
    
    context = {
        
    }
    
    return render(request, 'contato.html', context)