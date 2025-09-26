from .service import ProdutoService
from .models import Produto


dados_produto_valido = {
    "nome": "Teclado Mecânico Gamer",
    "preco": "350.50",
    "estoque": 15,
    "disponivel": True,
    "status": 1,
    "data_validade": "2028-12-31"
}

resultado, erro = ProdutoService.create_produto(dados_produto_valido)

print(erro)
print(resultado)