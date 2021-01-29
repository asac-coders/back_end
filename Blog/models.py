from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Blog(models.Model):
    first_name = models.CharField(max_length=64)
    Last_name = models.TextField()
    student_number = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image = models.URLField()
    

    def __str__(self):
        return self.first_name


   