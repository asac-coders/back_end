from django.contrib import admin

from .models import Blog
from .models import Projects, Ownership,Skils

# Register your models here.
admin.site.register(Blog)
admin.site.register(Projects)
admin.site.register(Ownership)
admin.site.register(Skils)

