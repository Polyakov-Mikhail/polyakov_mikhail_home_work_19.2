from django.urls import path, include
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductsListView, ContactsTemplateView, ProductDetailView
from django.conf import settings


app_name = CatalogConfig.name

urlpatterns = [
    path('homework19/', ProductsListView.as_view(), name="homework19"),
    path('homework19/contacts/', ContactsTemplateView.as_view(), name="contacts"),
    path('homework19/product/<int:pk>/', ProductDetailView.as_view(), name="product_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
