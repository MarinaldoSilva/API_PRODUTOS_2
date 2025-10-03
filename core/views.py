from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .service import ProdutoService
from .utils import get_status_errors


class ProdutoListCreateAPIView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        service = ProdutoService(user=request.user)
        """
        o service ao ser instanciado, já recebe o valor do request.user, e salva na variavel user no service a instânica da class, sendo assim não é mais necessário passar o valor no serializer.save(dono=user) toda vez que tiver que for salvar um produto no banco.
        """
        produto, erro = service.get_all_produtos_user()
        if erro:
            status_error = get_status_errors(erro)
            return Response(erro, status=status_error)
        return Response(produto, status=status.HTTP_200_OK)
    
    def post(self, request):
        service = ProdutoService(user=request.user)
        produto, erro = service.create_produto(request.data)
        if erro:
            status_error = get_status_errors(erro)
            return Response(erro, status=status_error)
        return Response(produto, status=status.HTTP_201_CREATED)
    
class ProdutoDetailAPIView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        service = ProdutoService(user=request.user)
        produto, erro = service.get_pk_produto_user(pk)

        if erro:
            status_error = get_status_errors(erro)
            return Response(erro, status=status_error)
        return Response(produto, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        service = ProdutoService(user=request.user)
        produto, erro = service.update_produto_user(pk, request.data, partial=True)
        if erro:
            status_error = get_status_errors(erro)
            return Response(erro, status=status_error)
        return Response(produto, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        service = ProdutoService(user=request.user)
        produto, erro = service.update_produto_user(pk, request.data)
        if erro:
            status_error = get_status_errors(erro)
            return Response(erro, status=status_error)
        return Response(produto, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        service = ProdutoService(user=request.user)
        produto, erro = service.deletar_produto_user(pk)
        if erro:
            status_error = get_status_errors(erro)
            return Response(erro, status=status_error)
        return Response(status=status.HTTP_204_NO_CONTENT)
