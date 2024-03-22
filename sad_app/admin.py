from django.contrib import admin
from sad_app.models import Membro
from sad_app.models import Publicacao
from sad_app.models import tipoPublicacao

# Register your models here.
admin.site.register(Membro)
admin.site.register(Publicacao)
admin.site.register(tipoPublicacao)

