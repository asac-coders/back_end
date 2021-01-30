from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView , CreateAPIView

from .serializer import BlogSerializer
from .models import Blog
from .permissions import PermissionsClass
# Create your views here.
class BlogListView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (PermissionsClass,)

class BlogDetailsView(RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (PermissionsClass,)

# class BlogCreateView(CreateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer  
#     permission_classes = (PermissionsClass,)
