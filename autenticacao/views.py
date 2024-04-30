from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Pessoa
import json

def cadastro(request):
  if request.method == 'GET':
    return render(request, 'cadastro/index.html')
  elif request.method == 'POST':
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    pessoa = Pessoa(nome=nome, 
                    email=email,
                    senha=senha)
    pessoa.save()

    return redirect('/autenticacao/cadastro')
  
  
def listar(request):
  pessoas = Pessoa.objects.all()

  if request.method == 'GET':
    return render(request, 'listar/listar.html')
  elif request.method == 'POST':
    nome = request.POST.get('nome')
    email = request.POST.get('email')

    if not nome and not email:
      return render(request, 'listar/listar.html', {'pessoas': pessoas})
    else:
      pessoa = Pessoa.objects.filter(nome=nome) | Pessoa.objects.filter(email=email)
      return render(request, 'listar/listar.html', {'pessoa': pessoa})
    

def alterar(request, id):
  if request.method == 'GET':
    return render(request, 'listar/alterar.html', {'id': id})
  if request.method == 'POST':
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    pessoa_alterar = Pessoa.objects.filter(id=id)[0]  # na posição '0', primeira e única posição da lista.

    pessoa_alterar.nome = nome
    pessoa_alterar.email = email
    pessoa_alterar.senha = senha

    pessoa_alterar.save()
    
    return render(request, 'listar/listar.html')
  

def excluir(request, id):
  pessoa_excluir = Pessoa.objects.filter(id=id)
  pessoa_excluir.delete()
  
  return render(request, 'listar/listar.html')