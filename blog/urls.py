from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('homework21/', BlogListView.as_view(), name='blog_list'),
    path('homework21/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('homework21/create/', BlogCreateView.as_view(), name='blog_create'),
    path('homework21/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('homework21//delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
    # path('activity/<int:pk>/', is_published, name='is_published'),
]
