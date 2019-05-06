from django.contrib import admin
from django.urls import path, include
from .views import HomePageView, CreatePostView, my_view

urlpatterns = [

    path('', my_view),
    path('home/', CreatePostView.as_view(), name='home'),
    path('feedback/', HomePageView.as_view(), name='feedback'),

]
