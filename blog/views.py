from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView #LV queryset for us in the database that we can list, detail brings the detail of one record
from .models import Post, BlogCategory, Comment
from .forms import BlogPostForm, EditForm, CommentForm
from django.urls import reverse_lazy

# Create your views here.
#def view_blog(request):
#    return render(request, 'blog.html')

class BlogView(ListView):
    model = Post
    template_name = 'blog.html'
    ordering = ['-blog_post_date'] #latest blog will be listed first

class BlogPostView(DetailView):
    model = Post
    template_name = 'blog_post.html'

class AddBlogPostView(CreateView):
    model = Post
    form_class = BlogPostForm
    template_name = 'add_blog_post.html'
    #fields = '__all__' #all fields

class UpdateBlogPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_blog_post.html'
    #fields = ['title', 'title_tag', 'body']

class DeleteBlogView(DeleteView):
    model = Post
    template_name = 'delete_blog_post.html'
    success_url = reverse_lazy('blog')

class AddCategoryView(CreateView):
    model = BlogCategory
    template_name = 'add_blog_category.html'
    fields = '__all__' #all fields

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-',' ')) #slugify urls to get rid of the space
    return render(request, 'categories_view.html', {'cats': cats.title().replace('-',' '), 'category_posts':category_posts})


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_blog_comment.html'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk'] #accessing pk of the blog to get id
        return super().form_valid(form)

    success_url = reverse_lazy('blog')
