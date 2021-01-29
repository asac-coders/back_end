from rest_framework import serializers

from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'first_name', 'Last_name', 'student_number', 'image')
        model = Blog