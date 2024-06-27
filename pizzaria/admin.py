from django.contrib import admin

from pizzaria.models import Cliente, Pizza, Pedido


class Clientes(admin.ModelAdmin):
    list_display = ('id','nome', 'telefone', 'endereco')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Cliente, Clientes)

class Pizzas(admin.ModelAdmin):
    list_display = ('id','nome', 'valor')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Pizza, Pizzas)

class Pedidos(admin.ModelAdmin):
    list_display = ('id','cliente', 'pizza', 'data', 'observacao')
    list_display_links = ('id', 'cliente')

admin.site.register(Pedido, Pedidos)
