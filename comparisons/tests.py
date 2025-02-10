from django.test import TestCase
from django.contrib.auth.models import User
from comparisons.models import Comparison
from products.models import Product, Category
from rest_framework import status


class ComparisonDetailViewTests(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username="test", password="pass"
            )
        self.client.login(username="test", password="pass")

        #  test category
        self.test_category = Category.objects.create(name="test")

        #  test products
        self.product1 = Product.objects.create(
            owner=self.test_user,
            name="Product1",
            price="10.00",
            category=self.test_category
        )
        self.product2 = Product.objects.create(
            owner=self.test_user,
            name="Product2",
            price="15.00",
            category=self.test_category
        )

        # comparison object
        self.comparison = Comparison.objects.create(owner=self.test_user)
        self.comparison.products.set([self.product1, self.product2])

    def test_retrieve_comparison(self):
        """Test retrieving a single comparison object."""
        url = f"/comparisons/{self.comparison.id}/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["owner"], self.test_user.username)

    def test_retrieve_comparison_with_invalid_id(self):
        """
        Test retrieving a comparison
        with an invalid ID should return 404.
        """

        url = "/comparisons/12345/"  # random id
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
