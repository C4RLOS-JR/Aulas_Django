from django.shortcuts import render
from django.http import HttpResponse
import json

def cadastro(request):
  if request.method == 'GET':
    return render(request, 'cadastro/index.html')
  elif request.method == 'POST':
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    return HttpResponse(json.dumps({'nome': nome, 'email': email}))