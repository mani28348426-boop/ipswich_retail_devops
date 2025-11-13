from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.home, name="home"),  # /
    path("products/", views.product_list, name="product_list"),  # /products/
    path("products/<int:pk>/", views.product_detail, name="product_detail"),  # /products/1/
    path("about/", views.about, name="about"),  # /about/
    path("contact/", views.contact, name="contact"),  # /contact/
    path("dashboard/products/", views.product_admin, name="product_admin"),  # /dashboard/products/
]
