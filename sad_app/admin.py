from django.contrib import admin
from sad_app.models import Membro
from sad_app.models import Publicacao
from sad_app.models import tipoPublicacao
from sad_app.models import Formacao
from sad_app.models import Nacionalidade

# Register your models here.
admin.site.register(Membro)
admin.site.register(Publicacao)
admin.site.register(tipoPublicacao)
admin.site.register(Formacao)
admin.site.register(Nacionalidade)
