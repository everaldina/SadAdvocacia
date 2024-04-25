from django.urls import path
from sad_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('publicacoes', views.publicacoes, name='publicacoes'),
    path('contato', views.contato, name='contato'),
    path('cadastro/publicacao', views.formulario_publicacao, name='formulario_publicacao'),
    path('cadastro/tipo-publicacao', views.tipoPublicacao, name='formulario_tipo_publicacao'),
    path('cadastro/membro', views.formulario_membro, name='formulario_membro'),
    path('cadastro/cargo', views.formulario_cargo, name='formulario_cargo'),
    path('cadastro/formacao', views.formulario_formacao, name='formulario_formacao'),
    path('cadastro/nacionalidade', views.formulario_nacionalidade, name='formulario_nacionalidade'),
    path('cadastro/instituicao', views.instituicao, name='formulario_instituicao'),
    path('cadastro/curso', views.curso, name='formulario_curso'),
    path('cadastro/nivel-formacao', views.nivelFormacao, name='formulario_nivel_formacao'),
    path('cadastro/modalidade', views.modalidade, name='formulario_modalidade'),
    path('cadastro', views.cadastro, name='cadastro')
]