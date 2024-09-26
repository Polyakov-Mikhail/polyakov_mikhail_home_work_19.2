from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from blog.models import Blog


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "content", "image")
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "content", "image")
    success_url = reverse_lazy('blog:blog_list')
