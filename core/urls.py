from django.urls import path
from .views import ProdutoDetailAPIView, ProdutoListCreateAPIView


urlpatterns = [
    path('produto/', ProdutoListCreateAPIView.as_view(), name='prod_list_create'),
    path('produto/<int:pk>/', ProdutoDetailAPIView.as_view(), name='prod_detail')
]