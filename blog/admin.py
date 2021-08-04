from django.contrib import admin

# Register your models here.
from .models import BlogAuthor,Blog

admin.site.register(BlogAuthor)
admin.site.register(Blog)
