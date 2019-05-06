from django.views.generic import ListView, CreateView
from django.views.generic import TemplateView

from django.shortcuts import redirect

from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpRequest

from .forms import PostForm
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')


def my_view(request):
    return redirect('login/')
