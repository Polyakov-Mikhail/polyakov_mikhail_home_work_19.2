from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, unit

app_name = CatalogConfig.name

urlpatterns = [
    path('homework19/', home, name="homework19"),
    path('homework19/contacts/', contacts, name="contacts"),
    path('homework19/unit/', unit, name="unit")
]
