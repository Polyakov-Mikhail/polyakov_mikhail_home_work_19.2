from django.urls import path
from Product.apps import ProductConfig

from Product.views import product

app_name = ProductConfig.name

urlpatterns = [
    path('', product, name='home')
]
