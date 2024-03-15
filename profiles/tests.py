from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import UserProfile

class ProfileViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        if not hasattr(self.user, 'userprofile'):
            self.profile = UserProfile.objects.create(user=self.user)


#class ProfileViewTests(TestCase):
    #def setUp(self):
        #self.user = User.objects.create_user(username='testuser', password='12345')
        #self.profile = UserProfile.objects.create(user=self.user)

    def test_profile_view_template(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_profile_update_form(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('profile'), {
            'default_phone_number': '123456789',
            'default_country': 'US',
            # Provide other required fields here
        })
        self.assertEqual(response.status_code, 200)  # Assuming successful redirect after form submission

    def test_profile_view_with_orders(self):
        # Assuming you have models named Order and LineItem related to UserProfile
        # Create orders related to the user profile
        # order = Order.objects.create(user=self.user, ...)
        # order.lineitems.create(...)

        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_order_history_view(self):
        # Assuming you have an Order model
        # Create an order to test the order history view
        # order = Order.objects.create(user=self.user, order_number='12345')
        
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('order_history', args=['12345']))
        self.assertEqual(response.status_code, 200)#fix
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
