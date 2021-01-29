from django.contrib import admin
from django.urls import path, include
from .views import MoviesDetailsView, MoviesListView

urlpatterns = [ 
       path('', MoviesListView.as_view(), name='movies'), 
       path('<int:pk>/', MoviesDetailsView.as_view(), name='movies_details'),
    ]