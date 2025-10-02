from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .service import ProdutoService


class ProdutoListCreateAPIView(APIView):

    def get(self, request):
        prod, erro = ProdutoService.get_all_produtos_user(request.user)
        if erro:
            return Response(erro, status=status.HTTP_400_BAD_REQUEST)
        return Response(prod, status=status.HTTP_200_OK)
    
    def post(self, request):
        prod, erro = ProdutoService.create_produto(request.data, request.user)
        if erro:
            return Response(erro, status=status.HTTP_400_BAD_REQUEST)
        return Response(prod, status=status.HTTP_201_CREATED)
    
class ProdutoDetailAPIView(APIView):

    def get(self, request, pk):
        prod, erro = ProdutoService.get_pk_produto_user(pk,request.user)
        if erro:
            return Response(erro, status=status.HTTP_404_NOT_FOUND)
        return Response(prod, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        prod, erro = ProdutoService.update_produto_user(pk, request.data, request.user, partial=True)
        if erro:
            return Response(erro, status=status.HTTP_404_NOT_FOUND)
        return Response(prod, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        prod, erro = ProdutoService.update_produto_user(pk, request.data, request.user)
        if erro:
            return Response(erro, status=status.HTTP_404_NOT_FOUND)
        return Response(prod, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        prod, erro = ProdutoService.deletar_produto_user(pk, request.user)
        if erro:
            return Response(erro, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
