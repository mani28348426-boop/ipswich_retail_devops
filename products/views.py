from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    # Show a few latest products on the homepage
    latest_products = Product.objects.all()[:4]
    return render(request, "products/home.html", {"latest_products": latest_products})


def product_list(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products": products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product_detail.html", {"product": product})


def about(request):
    return render(request, "products/about.html")
