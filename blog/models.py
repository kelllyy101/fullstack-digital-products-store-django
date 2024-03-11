from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #delete all blog posts
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author) #allows to see the author of the blog(object needs to be string)

    def get_absolute_url(self):
        return reverse('blog')