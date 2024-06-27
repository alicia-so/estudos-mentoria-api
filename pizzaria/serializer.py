from rest_framework import serializers
from pizzaria.models import Cliente, Pizza, Pedido

class BasePedidoSerializer(serializers.ModelSerializer):
  data = serializers.DateField(format='%d/%m/%Y')
  pizza = serializers.StringRelatedField()

  class Meta:
      model = Pedido
      fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'

class PedidoSerializer(BasePedidoSerializer):
    cliente = serializers.StringRelatedField()

class ListPedidosClienteSerializer(BasePedidoSerializer):
    class Meta(BasePedidoSerializer.Meta):
        model = Pedido
        fields = ['data', 'observacao', 'pizza']

class ListPizzaPedidosSerializer(serializers.ModelSerializer):
    pizza = serializers.ReadOnlyField(source='pizza.nome')
    cliente = serializers.ReadOnlyField(source='cliente.nome')
    class Meta:
        model = Pedido
        fields = ['pizza', 'cliente']