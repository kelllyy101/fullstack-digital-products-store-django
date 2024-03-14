from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.

class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default='best_you')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog') #on submit/post goes back to home


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #delete all blog posts
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    blog_post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='best_me')
    likes = models.ManyToManyField(User, related_name='blog_post_likes')
    blog_snippet = models.CharField(max_length=255, default='Click Title to Read')

    def __str__(self):
        return self.title + ' | ' + str(self.author) #allows to see the author of the blog(object needs to be string)

    def get_absolute_url(self):
        return reverse('blog') #on submit/post goes back to home