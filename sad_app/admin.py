from django.contrib import admin
from sad_app.models import Membro
from sad_app.models import Publicacao
from sad_app.models import tipoPublicacao
from sad_app.models import Formacao
from sad_app.models import Nacionalidade
from sad_app.models import Cargo
from sad_app.models import Instituicao
from sad_app.models import Curso
from sad_app.models import Modalidade
from sad_app.models import NivelFormacao
from sad_app.models import Usuario

# Register your models here.
admin.site.register(Membro)
admin.site.register(Publicacao)
admin.site.register(tipoPublicacao)
admin.site.register(Formacao)
admin.site.register(Nacionalidade)
admin.site.register(Cargo)
admin.site.register(Instituicao)
admin.site.register(Curso)
admin.site.register(Modalidade)
admin.site.register(NivelFormacao)
admin.site.register(Usuario)