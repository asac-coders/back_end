from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView , RetrieveAPIView
from .permissions import Permission
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializer import BlogSerializer
from .models import Blog

# Create your views here.
class BlogListView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permissions_classes = (Permission,IsAuthenticatedOrReadOnly ) 

class BlogDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permissions_classes = (Permission,IsAuthenticatedOrReadOnly) 