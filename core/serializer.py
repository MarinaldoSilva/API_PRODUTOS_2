from .models import Produto
from rest_framework import serializers

class ProdutoSerializer(serializers.ModelSerializer):

    dono = serializers.ReadOnlyField(source = 'dono.username')
    """
    source='is_available' está dizendo ao Serializer para exec o produto.is_available() para cada objeto Produto e usar o resultado como o valor do campo is_available.

    read_only=True: Isso significa que este campo é apenas para leitura. O Serializer não espera que este campo seja enviado na requisição POST ou PUT, o valor vem diretamente do banco de dados
    """
    disponibilidade = serializers.BooleanField(source = 'is_available', read_only=True)

    class Meta:
        model = Produto
        fields = [
            'id',
            'dono',
            'nome',
            'preco',
            'estoque',
            'disponivel',
            'status',
            'data_validade',
            'data_cadastro',
            'disponibilidade'
            ]
        read_only_fields = [
            'id',
            'dono',
            'data_cadastro'
            ]

        """
        quando chamado põe uma camada simples de validação do preço
        como é uma regra simples, não é necessário um service-layer
        """
        def validate_preco(self, preco):
            if preco <= 0:
                raise serializers.ValidationError("O preço do produto deve ser positivo.")
            return preco
        

