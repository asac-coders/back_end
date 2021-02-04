from django.contrib import admin
from django.urls import path
from django.conf.urls import include 
from rest_framework import routers
from .views import BlogDetailsView, BlogListView, ProjectView, ProjectDitailsView, SkilsView, SkilsDitailsView,UserViewSet

router = routers.DefaultRouter()
router.register('users',UserViewSet)
router.register('',BlogListView)
router.register('<int:pk>', BlogDetailsView)
router.register('projects', ProjectView)
router.register('projects/<int:pk>', ProjectDitailsView)
router.register('skils', SkilsView)
router.register('skils/<int:pk>', SkilsDitailsView)




urlpatterns = [
    path('',include(router.urls)),
]
