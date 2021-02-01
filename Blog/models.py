from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Skils(models.Model):
    student_number = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    html = models.BooleanField()
    css = models.BooleanField()
    js = models.BooleanField()
    react = models.BooleanField()
    nodejs = models.BooleanField()
    express = models.BooleanField()
    django = models.BooleanField()
    heroku = models.BooleanField()
    vercel = models.BooleanField()
    githab_pages = models.BooleanField()
    python = models.BooleanField()
    postgresql = models.BooleanField()
    mongodb = models.BooleanField()
    git = models.BooleanField()

    def __str__(self):
        return str(self.student_number)

class Projects(models.Model):
    student_number = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    project_name = models.CharField(max_length=63)
    live_url = models.URLField()
    github_url = models.URLField()
    description=models.TextField()
    features = models.TextField()
    def __str__(self):
        return str(self.project_name)


class Blog(models.Model):
    student_number = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,unique=True)
    first_name = models.CharField(max_length=64)
    Last_name = models.CharField(max_length=64)
    image = models.URLField(blank=True)
    about_me = models.TextField()
    skils = models.ForeignKey(Skils,on_delete=models.CASCADE)
    projects = models.ManyToManyField(Projects,  through= 'Ownership')
    email = models.EmailField(unique=True)
    github = models.URLField()
    linkedin = models.URLField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.Last_name)


class Ownership(models.Model):
    collection = models.ForeignKey(Projects, on_delete=models.CASCADE)
    owner = models.ForeignKey(Blog, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.owner)
   

