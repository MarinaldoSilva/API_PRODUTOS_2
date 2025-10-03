from .models import Produto
from .serializer import ProdutoSerializer
from django.utils import timezone


MSG_PRODUTO_NAO_LOCALIZADO  = "Produto não existe ou sem permissão de visualização"
error = "error"

class ProdutoService:
    """
    Toda vez que um ProdutoService é instanciado o valor de user que vem da request, esse valor é salvo no self.user, com isso precisamos usar o self.user ao inves do user da instancia.
    """
    def __init__(self, user):
        self.user = user #o valor de user instanciado esta na variavel user

    def _validar_preco(self, serializer):
        preco_item = serializer.validated_data.get('preco')
        if preco_item is not None and preco_item <= 0:
            return {'preco':['Preço não pode ser zero ou negativo']}
        return None
    
    def _data_validade(self, serializer):
        data_validade = serializer.validated_data.get('data_validade')
        if data_validade and data_validade < timezone.localdate():
            return {'data_validade':'[Validade do produto invalida.]'}
        return None
    
    def _verifica_estoque(self, validated_data):
        if 'estoque' in validated_data and validated_data['estoque'] == 0:
            validated_data['disponivel'] = False
            """Como dic em Py são mutáveis, quando o _verifica_estoque altera validated_data, ele altera a mesma posição memória de dados que está dentro do serializer. A alteração é feita diretamente no objeto original."""



    def get_all_produtos_user(self):
        try:
            produto = Produto.objects.filter(dono=self.user)
            serializer =ProdutoSerializer(produto, many=True)
            return serializer.data, None
        except Produto.DoesNotExist:
            return None, {error:MSG_PRODUTO_NAO_LOCALIZADO }

    def create_produto(self, data:dict):
        serializer = ProdutoSerializer(data=data)
        if not serializer.is_valid():
            return None, {error:serializer.errors}
        
        erro_preco = self._validar_preco(serializer)
        if erro_preco:
            return None, erro_preco
            
        erro_data = self._data_validade(serializer)
        if erro_data:
            return None, erro_data 
            
        dados_validados = serializer.validated_data

        self._verifica_estoque(dados_validados)
        serializer.save(dono=self.user)

        return serializer.data, None
        
    def update_produto_user(self, pk:int, data:dict, partial:bool =False):
        try:
            produto = Produto.objects.get(pk=pk, dono=self.user)
        except Produto.DoesNotExist:
            return None, {error:MSG_PRODUTO_NAO_LOCALIZADO }
        serializer = ProdutoSerializer(instance=produto, data=data, partial=partial)

        if serializer.is_valid():

            erro_preco = self._validar_preco(serializer)
            if erro_preco:
                return None, erro_preco
            
            erro_data = self._data_validade(serializer)
            if erro_data:
                return None, erro_data
            
            dados_validos = serializer.validated_data
            self._verifica_estoque(dados_validos)
            serializer.save()
            return serializer.data, None
        return None, serializer.errors
    
    def get_pk_produto_user(self, pk):
        try:
            produto = Produto.objects.get(pk=pk, dono=self.user)
            serializer = ProdutoSerializer(produto)
            return serializer.data, None
        except Produto.DoesNotExist:
            return None, {error:MSG_PRODUTO_NAO_LOCALIZADO}
        
    def deletar_produto_user(self, pk):
        try:
            produto = Produto.objects.get(pk=pk, dono=self.user)
            produto.delete()
            return True, None
        except Produto.DoesNotExist:
            return False, {error:MSG_PRODUTO_NAO_LOCALIZADO }
    

        
        