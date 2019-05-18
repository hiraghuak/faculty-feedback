from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, DetailView

from django.contrib import admin

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic import TemplateView

from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.http import HttpRequest

from .forms import PostForm
from .models import Post


class HomePageView(ListView):
    model = Post
    # template_name = 'home.html'


class CreatePostView(SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('feedback')

    def get_success_message(self, cleaned_data):
        return "form Saved Successfully"


def my_view(request):
    return redirect('login/')


class FeedbackList(ListView):
    model = Post
    template_name = 'updates/contact_list.html'
    #
    # def get_queryset(self, **kwargs):
    #     author = self.request.user
    #     object_list = Post.objects.filter(author=author)
    #     return Post.objects.filter(object_list=object_list)


class FeedbackDetail(DetailView):
    model = Post
    template_name = 'updates/contact_details.html'


class FeedbackCreate(CreateView):
    model = Post
    fields = "__all__"
    template_name = 'post.html'
    success_url = reverse_lazy('contact_list')


class FeedbackUpdate(UpdateView):
    model = Post
    template_name = 'updates/contact_form.html'
    fields = "__all__"
    success_url = reverse_lazy('contact_list')


class FeedbackDelete(DeleteView):
    model = Post
    template_name = 'updates/contact_confirm_delete.html'
    # fields = "__all__"
    success_url = reverse_lazy('contact_list')
