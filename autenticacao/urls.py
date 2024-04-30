from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('listar/', views.listar, name = 'listar'),
    path('alterar/<int:id>', views.alterar, name = 'alterar'),
    path('excluir/<int:id>', views.excluir, name = 'excluir'),

]