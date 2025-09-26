from django.db import models


class Produto(models.Model):

    class StatusProduto(models.IntegerChoices):
        EM_ESTOQUE = 1, 'Em Estoque'
        EM_REPOSICAO = 2, 'Em Reposição'
        FORA_DE_LINHA = 3, 'Fora de Linha'
    
    nome = models.CharField(max_length=150, unique=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()#somente valor positivo
    disponivel = models.BooleanField(default=True)
    status = models.IntegerField(
        choices=StatusProduto.choices,
        default=StatusProduto.EM_ESTOQUE
    )

    data_validade = models.DateField(null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"O produto '{self.nome }' tem estoque de {self.estoque}"


