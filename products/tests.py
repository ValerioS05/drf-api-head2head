from django.contrib.auth.models import User
from .models import Product, Category
from rest_framework import status
from rest_framework.test import APITestCase

class ProductListViewTests(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='test', password='pass')
        self.test_category = Category.objects.create(name='test')

    def test_can_list_products(self):
        Product.objects.create(
            owner=self.test_user,
            name='name',
            price='20.00',
            category=self.test_category
            )
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
