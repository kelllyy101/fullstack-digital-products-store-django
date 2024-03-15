from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!") #fix

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_blog_view(self):
        response = self.client.get(reverse("blog"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog.html")
        self.assertContains(response, "This is a test!")

    def test_blog_post_view(self):
        post = Post.objects.create(title="Test Post", body="This is a test post body.")
        response = self.client.get(reverse("blog_post", kwargs={"pk": post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog_post.html")
        self.assertContains(response, "Test Post")

    def test_add_blog_post_view(self):
        response = self.client.get(reverse("add_blog_post"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "add_blog_post.html")

    # Add more tests as needed for other views like UpdateBlogPost, DeleteBlogView, etc.
