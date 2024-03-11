from django.urls import path
from .views import BlogView, BlogPostView, AddBlogPostView, UpdateBlogPost

urlpatterns = [
    path('', BlogView.as_view(), name='blog'), #class based views
    path('post/<int:pk>', BlogPostView.as_view(), name='blog-post'),
    path('add_blog_post/', AddBlogPostView.as_view(), name ='add_blog_post'),
    path('update_blog_post/edit/<int:pk>', UpdateBlogPost.as_view(), name ='update_blog_post')
]