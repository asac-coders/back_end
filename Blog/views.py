from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

# from .serializer import MoviesSerializer
# from .models import Movies
# from .models import Movies
from .serializer import BlogSerializer
from .models import Blog

# Create your views here.
class BlogListView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer