from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, unit

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home),
    path('contacts/', contacts),
    path('unit/', unit)
]
