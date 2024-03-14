from django.urls import path
from .views import BlogView, BlogPostView, AddBlogPostView, UpdateBlogPost, DeleteBlogView, AddCategoryView, CategoryView, AddCommentView

urlpatterns = [
    path('', BlogView.as_view(), name='blog'), #class based views
    path('post/<int:pk>', BlogPostView.as_view(), name='blog_post'),
    path('add_blog_post/', AddBlogPostView.as_view(), name ='add_blog_post'),
    path('update_blog_post/edit/<int:pk>', UpdateBlogPost.as_view(), name ='update_blog_post'),
    path('delete_blog_post/delete/<int:pk>', DeleteBlogView.as_view(), name ='delete_blog_post'),
    path('add_blog_category/', AddCategoryView.as_view(), name ='add_blog_category'),
    path('category/<str:cats>/', CategoryView, name ='category_view'),
    path('add_blog_comment/<int:pk>/comment', AddCommentView.as_view(), name ='add_blog_comment'),
]