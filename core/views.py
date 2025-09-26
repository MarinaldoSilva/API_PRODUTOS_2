from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .service import ProdutoService


class ProdutoListCreateAPIView(APIView):

    def get(self, request):
        prod, erro = ProdutoService.get_all_produtos()
        if erro:
            return Response(erro, status=status.HTTP_400_BAD_REQUEST)
        return Response(prod, status=status.HTTP_200_OK)
    
    def post(self, request):
        prod, erro = ProdutoService.create_produto(request.data)
        if erro:
            return Response(erro, status=status.HTTP_400_BAD_REQUEST)
        return Response(prod, status=status.HTTP_200_OK)
    
class ProdutoDetailAPIView(APIView):

    def get(self, request, pk):
        prod, erro = ProdutoService.get_pk_produto(pk)
        if erro:
            return Response(erro, status=status.HTTP_404_NOT_FOUND)
        return Response(prod, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        prod, erro = ProdutoService.update_produto(pk, request.data, partial=True)
        if erro:
            return Response(erro, status=status.HTTP_404_NOT_FOUND)
        return Response(prod, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        prod, erro = ProdutoService.update_produto(pk, request.data)
        if erro:
            return Response(erro, status=status.HTTP_404_NOT_FOUND)
        return Response(prod, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        prod, erro = ProdutoService.deletar_produto(pk)
        if erro:
            return Response(erro, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
