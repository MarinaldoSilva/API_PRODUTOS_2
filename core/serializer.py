from .models import Produto
from rest_framework import serializers

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id','nome','preco', 'estoque','disponivel','status', 'data_validade', 'data_cadastro']
        read_only_fields = ['id','data_cadastro']