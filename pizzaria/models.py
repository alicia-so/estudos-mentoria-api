from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Pizza(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome
      
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    observacao = models.TextField(blank=True)

    def __str__(self):
        return f'{self.cliente} - {self.pizza}'