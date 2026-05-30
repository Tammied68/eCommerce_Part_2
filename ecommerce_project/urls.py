from django.contrib import admin
from django.urls import include, path

from planning_app.views import home
from stores.views import register, site_login

urlpatterns = [
    path("", home, name="home"),

    path("admin/", admin.site.urls),

    path("accounts/login/", site_login, name="login"),
    path("accounts/register/", register, name="register"),

    path("accounts/", include("django.contrib.auth.urls")),

    path("stores/", include("stores.urls")),
    path(
      
        "products/",
        include(("products.urls", "products"), namespace="products")
    ),
]