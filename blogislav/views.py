from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .models import Post

class BlogListVIew(ListView):
    model = Post
    template_name = 'home.html'



class BlogDeteilVIew(DetailView):
    model = Post
    template_name = 'post_detail.html'


class AddBlogView(CreateView):
    model = Post
    template_name = 'add_new.html'
    fields = ['author', 'title', 'body']

class BlogEditVIew(UpdateView):
    model = Post
    template_name = 'post_upgrade.html'
    fields = ['title', 'body']

class BLogDeleteme(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')



class SignUpViEW(generic.CreateView):
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    form_class = UserCreationForm
