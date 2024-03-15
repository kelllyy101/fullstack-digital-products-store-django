from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product

class BagViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a product for testing
        self.product = Product.objects.create(
            name='Test Product',
            price=10.00,
            sku='TEST123',
            description='Test description',
        )
    
    def test_bag_view(self):
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_bag(self):
        response = self.client.post(reverse('add_to_bag', args=[self.product.pk]), {'quantity': 1, 'redirect_url': '/'})
        self.assertEqual(response.status_code, 302)  # Redirect after adding to bag

        # Verify that the product is added to the bag
        bag = self.client.session.get('bag', {})
        self.assertTrue(str(self.product.pk) in bag)

    def test_adjust_bag(self):
        # Add a product to the bag
        self.client.post(reverse('add_to_bag', args=[self.product.pk]), {'quantity': 1, 'redirect_url': '/'})
        
        # Adjust the quantity
        response = self.client.post(reverse('adjust_bag', args=[self.product.pk]), {'quantity': 2})
        self.assertEqual(response.status_code, 302)  # Redirect after adjusting bag

        # Verify that the quantity is updated
        bag = self.client.session.get('bag', {})
        self.assertEqual(bag[str(self.product.pk)], 2)

    def test_remove_from_bag(self):
        # Add a product to the bag
        self.client.post(reverse('add_to_bag', args=[self.product.pk]), {'quantity': 1, 'redirect_url': '/'})
        
        # Remove the product from the bag
        response = self.client.post(reverse('remove_from_bag', args=[self.product.pk]))
        self.assertEqual(response.status_code, 200)

        # Verify that the product is removed from the bag
        bag = self.client.session.get('bag', {})
        self.assertFalse(str(self.product.pk) in bag)
