from django.urls import path
from . import views

app_name = "products"

urlpatterns = [

    # -------------------------
    # Part 1 Web Views
    # -------------------------

    path("", views.browse_products, name="list"),

    path(
        "<int:store_id>/products/",
        views.list_store_products,
        name="list_store_products",
    ),

    path(
        "<int:store_id>/products/add/",
        views.add_product,
        name="add_product",
    ),

    path(
        "edit/<int:product_id>/",
        views.edit_product,
        name="edit_product",
    ),

    path(
        "delete/<int:product_id>/",
        views.delete_product,
        name="delete_product",
    ),

    path(
        "detail/<int:product_id>/",
        views.product_detail,
        name="product_detail",
    ),

    path(
        "review/<int:product_id>/",
        views.leave_review,
        name="leave_review",
    ),

    path(
        "add-to-cart/<int:product_id>/",
        views.add_to_cart,
        name="add_to_cart",
    ),

    path(
        "cart/",
        views.cart_view,
        name="cart_view",
    ),

    path(
        "checkout/",
        views.checkout,
        name="checkout",
    ),

    path(
        "api/reviews/<int:product_id>/",
        views.product_reviews_api,
        name="product_reviews_api",
    ),
    
    # -------------------------
    # Part 2 API Views
    # -------------------------

    path(
        "api/store/<int:store_id>/",
        views.store_products_api,
        name="store_products_api",
    ),
]
