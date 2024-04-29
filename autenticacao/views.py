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
  nome = request.POST.get('nome')
  email = request.POST.get('email')
  print(nome)
  print(email)

  # if not nome and not email:
  #   return render(request, 'listar/index.html', {'pessoas': pessoas})
  # else:
  return render(request, 'listar/index.html')