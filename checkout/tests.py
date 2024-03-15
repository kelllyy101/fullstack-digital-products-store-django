from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse

class CheckoutPageTests(TestCase):
    def test_checkout_page_loads_correctly(self):
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')


class CheckoutProcessTests(TestCase):
    def test_successful_checkout_redirects_to_success_page(self):
        # Assume all required session data is set correctly for checkout
        response = self.client.post(reverse('checkout'), data={...})
        self.assertEqual(response.status_code, 302)  # 302 is a redirect status code
        # Check that the user is redirected to the checkout success page
        self.assertRedirects(response, reverse('checkout_success', args=[order_number]))


class CheckoutSuccessPageTests(TestCase):
    def test_checkout_success_page_loads_correctly(self):
        order_number = "123456789"  # Example order number
        response = self.client.get(reverse('checkout_success/<order_number>', args=[order_number]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')