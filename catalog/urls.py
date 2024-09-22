from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, unit

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name="homework19"),
    path('contacts/', contacts, name="contacts"),
    path('unit/', unit, name="unit")
]
