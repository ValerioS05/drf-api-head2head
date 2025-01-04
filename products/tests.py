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

class ProductDetailViewTest(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='test', password='pass')
        self.test_category = Category.objects.create(name='test')
        Product.objects.create(
            owner=self.test_user,
            name='name1',
            price='20.00',
            category=self.test_category
        )
        Product.objects.create(
            owner=self.test_user,
            name='name2',
            price='21.00',
            category=self.test_category
        )
    def test_retrieve_product_id(self):
        response = self.client.get('/products/1/')
        self.assertEqual(response.data['name'], 'name1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_product__with_invalid_id(self):
        response = self.client.get('/products/123/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)