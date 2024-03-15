from django.shortcuts import render
from sad_app.models import Membro

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
