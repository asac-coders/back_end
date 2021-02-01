from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView , CreateAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication

from .serializer import BlogSerializer, ProjectsSerializer, Skils_Serializer, UserSerializer
from .models import Blog,Projects , Skils
from .permissions import PermissionsClass
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes= (PermissionsClass,)

class BlogListView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (PermissionsClass,)

class BlogDetailsView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (PermissionsClass,)

class ProjectView(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer  
    permission_classes = (PermissionsClass,)

class ProjectDitailsView(viewsets.ModelViewSet ):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = (PermissionsClass,)

class SkilsView(viewsets.ModelViewSet):
    queryset = Skils.objects.all()
    serializer_class = Skils_Serializer  
    permission_classes = (PermissionsClass,)

class SkilsDitailsView(viewsets.ModelViewSet):
    queryset = Skils.objects.all()
    serializer_class = Skils_Serializer  
    permission_classes = (PermissionsClass,)

