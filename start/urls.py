from django.urls import path

from start.apps import StartConfig
from start.views import StartListView

app_name = StartConfig.name

urlpatterns = [
    path('', StartListView.as_view(), name='start'),
]
