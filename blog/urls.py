
from django.contrib import admin
from django.urls import path

from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('posts', views.Posts.as_view(), name='posts'),
    #path('books', views.Home.as_view(), name='books'),
    path('posts/<str:slug>', views.PostDetail.as_view(), name='post_detail'),
]
