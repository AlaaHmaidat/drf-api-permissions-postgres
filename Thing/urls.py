from django.contrib import admin
from django.urls import path
from .views import Thing_list,Thing_detail,Blog_detail,Blog_list

urlpatterns = [
    path('',Thing_list.as_view(), name='Thing_list' ),
    path('<int:pk>/',Thing_detail.as_view(),name='Thing_detail' ),
    path('blog/',Blog_list.as_view(), name='Blog_list' ),
    path('blog/<int:pk>/',Blog_detail.as_view(),name='Blog_detail' ),
]