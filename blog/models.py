from django.db import models

# Create your models here.

from datetime import date
from django.urls import reverse 
from django.contrib.auth.models import User 

class BlogAuthor(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=400, help_text="Enter your bio details here.")
    
    def __str__(self):
        return self.user.username
		
class Blog(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=2000, help_text="Enter you blog text here.")
    post_date = models.DateField(default=date.today)
    
    def __str__(self):
        return self.name