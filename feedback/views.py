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


# Listview
class HomePageView(ListView):
    model = Post
    # template_name = 'home.html'


# Redirect to login
def my_view(request):
    return redirect('login/')


# List view
def feedbacklist(request):
    if request.user.is_authenticated:
        my_qs = Post.objects.filter(user=request.user)
        my_qsall = Post.objects.all()

    template_name = 'updates/contact_list.html'
    context = {'object_list': my_qs, 'object_all': my_qsall}
    return render(request, template_name, context)


# Details View
class FeedbackDetail(DetailView):
    model = Post
    template_name = 'updates/contact_details.html'


# Crate form
def blog_post_create_view(request):
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


# Edit/Update form
class FeedbackUpdate(UpdateView):
    model = Post
    template_name = 'updates/contact_form.html'
    fields = [
        'CLASS_NAME',
        'SUBJECT',

        'NAME_OF_THE_LESSON',
        'INSTRUCTIONAL_OBJECTIVE_1',
        'INSTRUCTIONAL_OBJECTIVE_2',
        'INSTRUCTIONAL_OBJECTIVE_3',
        'INSTRUCTIONAL_OBJECTIVE_4',
        'INSTRUCTIONAL_OBJECTIVE_5',

        'AREA_OF_INTEREST',
        'STUDENTS_EXPERIENCE_VISUAL',
        'AUDITORY',
        'FINE_MOTOR',
        'GROSS_MOTOR',

        # TEACHING_POINT_1
        'TEACHING_POINT_1',
        'DOMAIN',
        'TYPE_OF_LEARNING_ACTIVITY_1',
        'LEARNING_ACTIVITY',
        'INTELLIGENCE_USED',
        'IMAGE_IF_ANY',
        'VIDEO_LINK_IF_ANY',
        'LEARNING_MATERIAL_USED',
        'ASSESSMENT_OF_LEARNING_ACTIVITY',


        # TEACHING_POINT_2
        'TEACHING_POINT_2',
        'DOMAIN_2',
        'TYPE_OF_LEARNING_ACTIVITY_2',
        'LEARNING_ACTIVITY_2',
        'INTELLIGENCE_USED_2',
        'IMAGE_IF_ANY_2',
        'VIDEO_LINK_IF_ANY_2',
        'LEARNING_MATERIAL_USED_2',
        'ASSESSMENT_OF_LEARNING_ACTIVITY_2',

        # TEACHING_POINT_3
        'TEACHING_POINT_3',
        'DOMAIN_3',
        'TYPE_OF_LEARNING_ACTIVITY_3',
        'LEARNING_ACTIVITY_3',
        'INTELLIGENCE_USED_3',
        'IMAGE_IF_ANY_3',
        'VIDEO_LINK_IF_ANY_3',
        'LEARNING_MATERIAL_USED_3',
        'ASSESSMENT_OF_LEARNING_ACTIVITY_3',

        # TEACHING_POINT_4
        'TEACHING_POINT_4',
        'DOMAIN_4',
        'TYPE_OF_LEARNING_ACTIVITY_4',
        'LEARNING_ACTIVITY_4',
        'INTELLIGENCE_USED_4',
        'IMAGE_IF_ANY_4',
        'VIDEO_LINK_IF_ANY_4',
        'LEARNING_MATERIAL_USED_4',
        'ASSESSMENT_OF_LEARNING_ACTIVITY_4',

        # TEACHING_POINT_5
        'TEACHING_POINT_5',
        'DOMAIN_5',
        'TYPE_OF_LEARNING_ACTIVITY_5',
        'LEARNING_ACTIVITY_5',
        'INTELLIGENCE_USED_5',
        'IMAGE_IF_ANY_5',
        'VIDEO_LINK_IF_ANY_5',
        'LEARNING_MATERIAL_USED_5',
        'ASSESSMENT_OF_LEARNING_ACTIVITY_5',



        # FINAL FORM
        'HOMEWORK',
        'COMMENTS',
        'STATUS',

        'publish_date',
    ]
    success_url = reverse_lazy('contact_list')


class FeedbackDelete(DeleteView):
    model = Post
    template_name = 'updates/contact_confirm_delete.html'
    # fields = "__all__"
    success_url = reverse_lazy('contact_list')
