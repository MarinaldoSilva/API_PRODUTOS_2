from .models import Produto
from .serializer import ProdutoSerializer
from django.utils import timezone

class ProdutoService:

    @staticmethod
    def _validar_preco(serializer):
        preco_item = serializer.validated_data.get('preco')
        if preco_item is not None and preco_item <= 0:
            return {'preco':['Preço não pode ser zero ou negativo']}
        return None
    
    @staticmethod
    def _data_validade(serializer):
        data_validade = serializer.validated_data.get('data_validade')
        if data_validade and data_validade < timezone.localdate():
            return {'data_validade':'[Validade do produto invalida.]'}
        return None
    
    @staticmethod
    def _verifica_estoque(validated_data):
        if 'estoque' in validated_data and validated_data['estoque'] == 0:
            validated_data['disponivel'] = False
            """Como dic em Py são mutáveis, quando o _verifica_estoque altera validated_data, ele altera a mesma posição memória de dados que está dentro do serializer. A alteração é feita diretamente no objeto original."""

    @staticmethod
    def get_all_produtos():
        produto = Produto.objects.all()
        seri =ProdutoSerializer(produto, many=True)
        return seri.data, None
    
    @staticmethod
    def create_produto(data):
        seri = ProdutoSerializer(data=data)
        if not seri.is_valid():
            return None, seri.errors
        
        erro_preco = ProdutoService._validar_preco(seri)
        if erro_preco:
            return None, erro_preco
            
        erro_data = ProdutoService._data_validade(seri)
        if erro_data:
            return None, erro_data 
            
        dados_validados = seri.validated_data

        ProdutoService._verifica_estoque(dados_validados)
        seri.save()

        return seri.data, None
        
        
    @staticmethod
    def update_produto(pk, data, partial=False):
        try:
            produto = Produto.objects.get(pk=pk)
        except Produto.DoesNotExist:
            return None, {"errors":"Produto não localizado"}
        seri = ProdutoSerializer(instance=produto, data=data, partial=partial)

        if seri.is_valid():

            erro_preco = ProdutoService._validar_preco(seri)
            if erro_preco:
                return None, erro_preco
            
            erro_data = ProdutoService._data_validade(seri)
            if erro_preco:
                return None, erro_preco
            
            dados_validos = seri.validated_data
            ProdutoService._verifica_estoque(dados_validos)
            seri.save()
            return seri.data, None
        return None, seri.errors
    
    @staticmethod
    def get_pk_produto(pk):
        try:
            produto = Produto.objects.get(pk=pk)
            seri = ProdutoSerializer(produto)
            return seri.data, None
        except Produto.DoesNotExist:
            return None, {"errors":"Produto não localizado"}
        

    @staticmethod
    def deletar_produto(pk):
        try:
            produto = Produto.objects.get(pk=pk)
            produto.delete()
            return True, None
        except Produto.DoesNotExist:
            return True, {"errors":"Produto não localizado"}
    

        
        