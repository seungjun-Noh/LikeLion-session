import email
from django.db import models
from django.forms import IntegerField


class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=128)    
    checkbox = models.BooleanField(default=False)

    def __str__(self):
        return self.title
