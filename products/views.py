from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Product
from .forms import ProductForm


def home(request):
    """Public home page."""
    latest_products = Product.objects.all()[:4]
    return render(request, "products/home.html", {"latest_products": latest_products})


def product_list(request):
    """Public products list page."""
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products": products})


def product_detail(request, pk):
    """Public product detail page."""
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product_detail.html", {"product": product})


def about(request):
    """Public about page."""
    return render(request, "products/about.html")


def contact(request):
    """Public contact page."""
    return render(request, "products/contact.html")


@login_required
def product_admin(request):
    """
    Custom admin page: single page to Create, Update, and Delete products.
    """
    edit_product = None
    products = Product.objects.all().order_by("-created_at")

    # If user clicked "Edit", get that product for pre-filling the form
    edit_id = request.GET.get("edit")
    if edit_id:
        edit_product = get_object_or_404(Product, pk=edit_id)

    if request.method == "POST":
        # Delete action
        delete_id = request.POST.get("delete_id")
        if delete_id:
            product = get_object_or_404(Product, pk=delete_id)
            product.delete()
            return redirect("products:product_admin")

        # Update action (has product_id in POST)
        product_id = request.POST.get("product_id")
        if product_id:
            product = get_object_or_404(Product, pk=product_id)
            form = ProductForm(request.POST, instance=product)
        else:
            # Create action
            form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("products:product_admin")
    else:
        # GET request – show empty form or pre-filled form (for edit)
        if edit_product:
            form = ProductForm(instance=edit_product)
        else:
            form = ProductForm()

    context = {
        "form": form,
        "products": products,
        "edit_product": edit_product,
    }
    return render(request, "products/product_admin.html", context)
