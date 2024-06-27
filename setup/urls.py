from django.contrib import admin
from django.urls import path, include
from pizzaria.views import (
  ClienteViewSet,
  PizzaViewSet,
  PedidoViewSet,
  ListPedidosCliente,
  ListPizzaPedidos
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet, basename='Cliente')
router.register('pizzas', PizzaViewSet, basename='Pizza')
router.register('pedidos', PedidoViewSet, basename='Pedido')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('cliente/<int:pk>/pedidos/', ListPedidosCliente.as_view(), name='pedidos_cliente'),
    path('pizza/<int:pk>/pedidos/', ListPizzaPedidos.as_view(), name='pedidos_pizza')
]
