from django.urls import path
from blog.apps import BlogConfig
from blog.views import start

app_name = BlogConfig.name

urlpatterns = [
    path('', start, name='start'),
]
