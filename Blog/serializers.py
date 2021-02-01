from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import Blog, Projects,Skils

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'first_name', 'Last_name', 'student_number', 'image', 'about_me','skils' ,'github', 'linkedin', 'projects')
        model = Blog

class ProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'student_number', 'project_name', 'live_url', 'github_url', 'description','features')
        model = Projects


class Skils_Serializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'student_number', 'html','css', 'js', 'react', 'nodejs', 'express','django', 'heroku', 'vercel',  'githab_pages', 'python', 'postgresql', 'mongodb', 'git' )
        model = Skils



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs={'password':{'write_only':True, 'required':True}}
    
    def create(self,validate_data):
        user = User.objects.create_user(**validate_data)
        Token.objects.create(user=user)
        return user