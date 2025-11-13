from django.test import TestCase
from django.urls import reverse
from .models import Product


class ProductModelTests(TestCase):
    def test_product_str_returns_name(self):
        product = Product.objects.create(
            name="Test Product",
            description="A test product",
            price=9.99,
            stock=5,
        )
        self.assertEqual(str(product), "Test Product")


class ProductViewTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="A test product",
            price=9.99,
            stock=5,
        )

    def test_home_page_status_code(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Modern E-commerce")

    def test_product_list_page_displays_products(self):
        url = reverse("products:product_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")

    def test_product_detail_page(self):
        url = reverse("products:product_detail", args=[self.product.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")

    def test_about_page_status_code(self):
        url = reverse("products:about")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status_code(self):
        url = reverse("products:contact")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
