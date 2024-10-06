from django.urls import path
from Product.apps import ProductConfig

from Product.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = ProductConfig.name

urlpatterns = [
    path('homework20/', ProductListView.as_view(), name='home'),
    path('homework20/products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('homework20/create/', ProductCreateView.as_view(), name='product_create'),
    path('homework20/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('homework20/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
]
