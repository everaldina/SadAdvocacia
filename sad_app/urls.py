from django.urls import path
from sad_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('publicacoes', views.publicacoes, name='publicacoes'),
    path('contato', views.contato, name='contato')
]