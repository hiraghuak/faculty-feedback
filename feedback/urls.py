from django.contrib import admin
from django.urls import path, include
from .views import HomePageView, CreatePostView, my_view, \
    FeedbackList, \
    FeedbackDetail, \
    FeedbackCreate, \
    FeedbackUpdate, \
    FeedbackDelete

urlpatterns = [

    path('', my_view),

    path('home/', FeedbackList.as_view(), name='home'),

    path('feedback/', HomePageView.as_view(), name='feedback'),

    path('create', FeedbackCreate.as_view(), name='contact_create'),

    path('list', FeedbackList.as_view(), name='contact_list'),
    path('contact/<int:pk>', FeedbackDetail.as_view(), name='contact_detail'),
    path('update/<int:pk>', FeedbackUpdate.as_view(), name='contact_update'),
    path('delete/<int:pk>', FeedbackDelete.as_view(), name='contact_delete'),

]
