from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Cargos, Pessoa

def cadastro(request):
  if request.method == 'GET':
    return render(request, 'cadastro/index.html')
  elif request.method == 'POST':
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    cargo = request.POST.get('cargo')
    cargo = Cargos.objects.get(id=cargo)

    pessoa = Pessoa(nome=nome, 
                    email=email,
                    senha=senha,
                    cargo=cargo)
    pessoa.save()

    return render(request, 'cadastro/index.html', {'status': '0'})
  
  
def listar(request):
  if request.method == 'GET':
    return render(request, 'listar/listar.html')
  elif request.method == 'POST':
    nome = request.POST.get('nome')
    email = request.POST.get('email')

    if nome or email:
      if nome and email:
        pessoas = Pessoa.objects.filter(nome=nome).filter(email=email)
      else:
        pessoas = Pessoa.objects.filter(nome=nome) | Pessoa.objects.filter(email=email).all()
    else:
      pessoas = Pessoa.objects.all()
    
    return render(request, 'listar/listar.html', {'pessoas': pessoas})

def alterar(request, id):
  if request.method == 'GET':
    return render(request, 'listar/alterar.html', {'id': id})
  if request.method == 'POST':
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    cargo = request.POST.get('cargo')
    cargo = Cargos.objects.get(id=cargo)
    # pessoa_alterar = Pessoa.objects.filter(id=id)[0]  # na posição '0', primeira e única posição da lista.
    pessoa_alterar = Pessoa.objects.get(id=id)

    if nome:
      pessoa_alterar.nome = nome
    if email:
      pessoa_alterar.email = email
    if senha:
      pessoa_alterar.senha = senha
    if cargo:
      pessoa_alterar.cargo = cargo
    pessoa_alterar.save()
    
    return render(request, 'listar/listar.html', {'status': '1'})
  

def excluir(request, id):
  pessoa_excluir = Pessoa.objects.filter(id=id)
  pessoa_excluir.delete()
  
  return render(request, 'listar/listar.html', {'status': '2'})