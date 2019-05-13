from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic import TemplateView

from django.shortcuts import redirect

from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpRequest

from .forms import PostForm, ContactForm
from .models import Post, Contact


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
