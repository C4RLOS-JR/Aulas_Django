from django.db import models

class Cargos(models.Model):
  nome = models.CharField(max_length=20)

  def __str__(self):
    return self.nome
  

class Pessoa(models.Model):
  nome = models.CharField(max_length=100)
  email = models.EmailField()
  senha = models.CharField(max_length=100)
  cargo = models.ForeignKey(Cargos, on_delete=models.DO_NOTHING)

  def __str__(self):
    return self.nome
  
  
class Pedido(models.Model):
  nome = models.CharField(max_length=50)
  quantidade = models.IntegerField()
  descricao = models.TextField()
  pessoa = models.ForeignKey(Pessoa, on_delete=models.DO_NOTHING)

  def __str__(self):
    return self.nome