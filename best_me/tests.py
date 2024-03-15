from django.test import TestCase
from django.urls import reverse


class BaseAppTests(TestCase):
    def test_admin_url(self):
        response = self.client.get(reverse('admin:index'))
        self.assertEqual(response.status_code, 302)  # Ensure redirection to login page

    def test_accounts_url(self):
        response = self.client.get(reverse('account_login'))
        self.assertEqual(response.status_code, 200)  # Ensure login page is accessible

    def test_home_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)  # Ensure home page is accessible
