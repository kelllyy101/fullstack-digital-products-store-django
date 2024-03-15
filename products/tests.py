from django.test import TestCase
from django.contrib.auth.models import User 
from django.urls import reverse
from .models import Product, Category

class ProductViewTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', email='test@example.com', password='password'
        )

        # Create some categories
        self.category1 = Category.objects.create(name='Category 1', friendly_name='Category 1')
        self.category2 = Category.objects.create(name='Category 2', friendly_name='Category 2')

        # Create some test products
        self.product1 = Product.objects.create(name='Product 1', price=10.0, category=self.category1)
        self.product2 = Product.objects.create(name='Product 2', price=20.0, category=self.category2)

    def test_all_products_view(self):
        # Test the all products view
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(self.product1 in response.context['products'])
        self.assertTrue(self.product2 in response.context['products'])

    def test_product_description_view(self):
        # Test the product description view
        response = self.client.get(reverse('product_description', args=[self.product1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_description.html')
        self.assertEqual(response.context['product'], self.product1)

    def test_add_product_view(self):
        # Log in as the test user
        self.client.login(username='testuser', password='password')

        # Test the add product view
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 302) 
        self.assertTemplateUsed(response, 'products/product_description.html')#fix

        # Add a product
        response = self.client.post(reverse('add_product'), {
            'name': 'New Product',
            'price': 15.0,
            'category': self.category1.id,
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

        # Ensure that the product was added
        self.assertTrue(Product.objects.filter(name='New Product').exists())

    def test_edit_product_view(self):
        # Log in as the test user
        self.client.login(username='testuser', password='password')

        # Test the edit product view
        response = self.client.get(reverse('edit_product', args=[self.product1.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'products/edit_product.html')#fix

        # Edit the product
        response = self.client.post(reverse('edit_product', args=[self.product1.id]), {
            'name': 'Edited Product',
            'price': 25.0,
            'category': self.category2.id,
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

        # Ensure that the product was edited
        edited_product = Product.objects.get(id=self.product1.id)
        self.assertEqual(edited_product.name, 'Edited Product')
        self.assertEqual(edited_product.price, 25.0)
        self.assertEqual(edited_product.category, self.category2)

    def test_delete_product_view(self):
        # Log in as the test user
        self.client.login(username='testuser', password='password')

        # Test the delete product view
        response = self.client.post(reverse('delete_product', args=[self.product1.id]))
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

        # Ensure that the product was deleted
        self.assertFalse(Product.objects.filter(id=self.product1.id).exists())#fix
