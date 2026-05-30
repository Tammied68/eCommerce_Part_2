from django.urls import path
from . import views

urlpatterns = [

    # -------------------------
    # Part 1 Web Views
    # -------------------------

    path("", views.store_list, name="store_list"),

    path("register/", views.register, name="register"),

    path("create/", views.create_store, name="create_store"),
    path("edit/<int:store_id>/", views.edit_store, name="edit_store"),
    path("delete/<int:store_id>/", views.delete_store, name="delete_store"),

    # -------------------------
    # Part 2 API Views
    # -------------------------

    path("api/", views.list_stores, name="list_stores"),

    path(
        "api/create/",
        views.create_store_api,
        name="create_store_api",
    ),

    path(
        "api/<int:store_id>/",
        views.get_store,
        name="get_store",
    ),

    path(
        "api/vendor/<int:vendor_id>/",
        views.vendor_stores,
        name="vendor_stores",
    ),
]
