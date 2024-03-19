from django.test import TestCase
from django.urls import reverse  

# Create your tests here.


""" class HomepageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home/index.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1> Get ready to be the Best You!</h1>")
        self.assertNotContains(response, "Not on the page") """

from django.test import SimpleTestCase
from django.urls import reverse

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home/index.html", "base.html")

    def test_main_heading_present(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Get ready to be the Best You!")

    def test_shop_now_button_present(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "SHOP NOW")

    def test_carousel_present(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "carouselExampleIndicators")

    def test_product_images_present(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "media/pexels-cup-of-couple-6177588.jpg")
        self.assertContains(response, "media/pexels-ken-tomita-389818.jpg")
        self.assertContains(response, "media/pexels-ketut-subiyanto-4132326.jpg")

    def test_product_names_present(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Journaling")
        self.assertContains(response, "Meditation")
