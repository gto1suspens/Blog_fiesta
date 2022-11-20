from django.shortcuts import render
from django.views.generic import ListView,DeleteView
# Create your views here.
from .models import Post

class BlogListVIew(ListView):
    model = Post
    template_name = 'home.html'

    context_object_name = 'blog_list'

class BlogDeteilVIew(DeleteView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post_detail'