from django.urls import path
from sad_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('publicacoes', views.publicacoes, name='publicacoes'),
    path('contato', views.contato, name='contato'),
    path('formulario-membro', views.formulario_membro, name='formulario_membro'),
    path('formulario-publicacao', views.formulario_publicacao, name='formulario_publicacao'),
    path('formulario-formacao', views.formulario_formacao, name='formulario_formacao')
]