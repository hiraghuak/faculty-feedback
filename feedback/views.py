from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import admin

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic import TemplateView

from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse_lazy
from django.http import HttpRequest
from django.db import models

from .forms import PostForm
from .models import Post


class HomePageView(ListView):
    model = Post
    # template_name = 'home.html'


# class CreatePostView(SuccessMessageMixin, CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'post.html'
#     success_url = reverse_lazy('feedback')
#
#     def get_success_message(self, cleaned_data):
#         return "form Saved Successfully"


def my_view(request):
    return redirect('login/')


def feedbacklist(request):
    if request.user.is_authenticated:
        my_qs = Post.objects.filter(user=request.user)
    template_name = 'updates/contact_list.html'
    context = {'object_list': my_qs}
    return render(request, template_name, context)


class FeedbackDetail(DetailView):
    model = Post
    template_name = 'updates/contact_details.html'


# class FeedbackCreate(CreateView):
#     # model = Post
#     form_class = PostForm
#     queryset = Post.objects.all()
#     template_name = 'post.html'
#     success_url = reverse_lazy('contact_list')
#
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return super().form_valid(form)


def blog_post_create_view(request):
    # create objects
    # ? use a form
    # request.user -> return something
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = PostForm()
        messages.success(request, 'Form submission successful')
    template_name = 'post.html'
    context = {'form': form}
    return render(request, template_name, context)


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
