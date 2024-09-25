from django.urls import path
from Product.apps import ProductConfig

from Product.views import ProductListView, ProductDetailView

app_name = ProductConfig.name

urlpatterns = [
    path('homework20/', ProductListView.as_view(), name='home'),
    path('homework20/products/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
]
