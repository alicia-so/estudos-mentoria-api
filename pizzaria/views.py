from django.http import JsonResponse
from rest_framework import viewsets, generics

from pizzaria.models import Cliente, Pizza, Pedido

from .serializer import (
  ClienteSerializer, 
  PizzaSerializer, 
  PedidoSerializer,
  ListPedidosClienteSerializer,
  ListPizzaPedidosSerializer
) 

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ClienteViewSet(viewsets.ModelViewSet):
  """ Exibindo todos os clientes """
  queryset = Cliente.objects.all()
  serializer_class = ClienteSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]
  
class PizzaViewSet(viewsets.ModelViewSet):
  """ Exibindo todos os sabores de pizzas """
  queryset = Pizza.objects.all()
  serializer_class = PizzaSerializer

class PedidoViewSet(viewsets.ModelViewSet):
  """ Exibindo todos os pedidos """
  queryset = Pedido.objects.all()
  serializer_class = PedidoSerializer

class ListPedidosCliente(generics.ListAPIView):
  """ Exibindo todos os pedidos de um cliente """
  def get_queryset(self):
    queryset = Pedido.objects.filter(cliente_id=self.kwargs['pk'])
    return queryset
  serializer_class = ListPedidosClienteSerializer

class ListPizzaPedidos(generics.ListAPIView):
  """ Exibindo todos os pedidos de uma pizza """
  def get_queryset(self):
    queryset = Pedido.objects.filter(pizza_id=self.kwargs['pk'])
    return queryset
  serializer_class = ListPizzaPedidosSerializer