from django.contrib import admin
from django.urls import path, include
from .views import (HomePageView,
                    my_view,
                    FeedbackDetail,
                    FeedbackUpdate,
                    FeedbackDelete,
                    feedbacklist,
                    # FeedbackCreate,
                    blog_post_create_view
                    )

urlpatterns = [

    path('', my_view),

    path('home/', feedbacklist, name='home'),
    path('list', feedbacklist, name='contact_list'),


    path('feedback/', HomePageView.as_view(), name='feedback'),

    # path('create', FeedbackCreate.as_view(), name='contact_create'),
    path('create', blog_post_create_view, name='contact_create'),


    path('contact/<int:pk>', FeedbackDetail.as_view(), name='contact_detail'),
    path('update/<int:pk>', FeedbackUpdate.as_view(), name='contact_update'),
    path('delete/<int:pk>', FeedbackDelete.as_view(), name='contact_delete'),

]
