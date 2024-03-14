from django.contrib import admin
from .models import Post, BlogCategory, Comment

# Register your models here.

admin.site.register(Post)
admin.site.register(BlogCategory)
admin.site.register(Comment)

