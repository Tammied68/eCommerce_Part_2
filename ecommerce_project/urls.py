from django.contrib import admin
from django.urls import include, path

from planning_app.views import home
from stores.views import register, site_login

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),

    # Custom storefront login
    path("accounts/login/", site_login, name="login"),

    # Custom registration
    path("accounts/register/", register, name="register"),

    # Django auth routes: logout, password reset, etc.
    path("accounts/", include("django.contrib.auth.urls")),

    # App routes
    path("stores/", include("stores.urls")),
    path("products/", include(("products.urls", "products"), namespace="products")),
]