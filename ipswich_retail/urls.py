from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from products import views as product_views

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),

    # Auth: login/logout
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(next_page="home"),
        name="logout",
    ),

    # Home page
    path("", product_views.home, name="home"),

    # Products app URLs (for /products/, /about/, /contact/, /dashboard/products/)
    path("", include("products.urls")),
]
