from django import forms
from .models import Post, BlogCategory, Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'blog_snippet', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), #from Bootstrap instead of static files
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'blog_snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'image:': forms.URLField(),
        }

class EditForm(forms.ModelForm): #form to edit blog
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'blog_snippet', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), #from Bootstrap instead of static files
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'blog_snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'image:': forms.URLField()
        }


class CommentForm(forms.ModelForm): 
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}), #from Bootstrap instead of static files
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }