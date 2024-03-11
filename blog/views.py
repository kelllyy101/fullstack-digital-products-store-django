from django.shortcuts import render
from django.views.generic import ListView, DetailView #LV queryset for us in the database that we can list, detail brings the detail of one record
from .models import Post
# Create your views here.
#def view_blog(request):
#    return render(request, 'blog.html')

class BlogView(ListView):
    model = Post
    template_name = 'blog.html'

class BlogPostView(DetailView):
    model = Post
    template_name = 'blog_post.html'