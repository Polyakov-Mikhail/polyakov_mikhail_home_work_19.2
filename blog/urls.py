from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView

app_name = BlogConfig.name

urlpatterns = [
    path('homework21/', BlogListView.as_view(), name='blog_list'),
    path('homework21/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('homework21/create/', BlogCreateView.as_view(), name='blog_create'),
    path('homework21/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    # path('delete/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    # path('activity/<int:pk>/', is_published, name='is_published'),
]
