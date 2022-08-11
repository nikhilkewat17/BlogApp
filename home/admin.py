from django.contrib import admin

# Register your models here.
from .models import BlogModel
from .models import Profile

admin.site.register(BlogModel)
admin.site.register(Profile)