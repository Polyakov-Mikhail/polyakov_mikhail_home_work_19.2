from django.urls import path
from Product.apps import ProductConfig

from Product.views import product, product_detail

app_name = ProductConfig.name

urlpatterns = [
    path('homework20/', product, name='home'),
    path('homework20/products/<int:pk>/', product_detail, name='product_detail')
]
