from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['dono','nome','preco','estoque','disponivel','data_validade','data_cadastro']
    search_fields = ['dono__username','nome','preco','estoque','disponivel','data_validade','data_cadastro']
    
