from django.contrib import admin
from django.urls import path, include
from .views import BlogDetailsView, BlogListView

urlpatterns = [ 
       path('', BlogListView.as_view(), name='blog'), 
       path('/<int:pk>/', BlogDetailsView.as_view(), name='blog_details'),
    ]