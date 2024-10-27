from django.urls import path
from django.views.decorators.cache import cache_page

from Product.apps import ProductConfig

from Product.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    CategoryListView

app_name = ProductConfig.name

urlpatterns = [
    path('homework20/', ProductListView.as_view(), name='home'),
    path('homework20/category/', CategoryListView.as_view(), name='category_list'),
    path('homework20/products/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('homework20/create/', ProductCreateView.as_view(), name='product_create'),
    path('homework20/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('homework20/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
]
