from django.urls import path
from .views import BlogView, BlogPostView

urlpatterns = [
    path('', BlogView.as_view(), name='blog'), #class based views
    path('post/<int:pk>', BlogPostView.as_view(), name='blog-post'),
]