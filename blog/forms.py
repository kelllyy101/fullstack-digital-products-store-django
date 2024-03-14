from django import forms
from .models import Post, BlogCategory, Comment

choices = BlogCategory.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'blog_snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), #from Bootstrap instead of static files
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'blog_snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm): #form to edit blog
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'blog_snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), #from Bootstrap instead of static files
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'blog_snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm): 
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}), #from Bootstrap instead of static files
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }