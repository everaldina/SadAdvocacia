from django.shortcuts import render
from sad_app.models import Membro

# Create your views here.
def home(request):
    equipe = Membro.objects.order_by('id')
    context = {
        'equipe': equipe
    }
    return render(request, 'index.html', context)
