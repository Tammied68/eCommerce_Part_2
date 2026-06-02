"""
Views for the stores application.

Includes:
- Part 1 web views for vendor store management and registration/login
- Part 2 REST API views for stores
"""

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.shortcuts import get_object_or_404, redirect, render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import RegisterForm
from .models import Profile, Store
from .serializers import StoreSerializer


@login_required
def store_list(request):
    """Display stores owned by the logged-in vendor."""

    is_vendor = request.user.groups.filter(name="Vendors").exists()

    if not is_vendor:
        return redirect("products:list")

    stores = Store.objects.filter(vendor=request.user)

    return render(request, "stores/store_list.html", {"stores": stores})


@login_required
def create_store(request):
    """Allow vendors to create a new store through the website."""

    is_vendor = request.user.groups.filter(name="Vendors").exists()

    if not is_vendor:
        messages.error(request, "Only vendors can create a store.")
        return redirect("products:list")

    if request.method == "POST":
        Store.objects.create(
            vendor=request.user,
            name=request.POST["name"],
            description=request.POST["description"],
        )
        return redirect("store_list")

    return render(request, "stores/create_store.html")


@login_required
def edit_store(request, store_id):
    """Edit an existing store owned by the logged-in vendor."""

    is_vendor = request.user.groups.filter(name="Vendors").exists()

    if not is_vendor:
        return redirect("products:list")

    store = get_object_or_404(Store, id=store_id, vendor=request.user)

    if request.method == "POST":
        store.name = request.POST["name"]
        store.description = request.POST["description"]
        store.save()
        return redirect("store_list")

    return render(request, "stores/edit_store.html", {"store": store})


@login_required
def delete_store(request, store_id):
    """Delete an existing store owned by the logged-in vendor."""

    is_vendor = request.user.groups.filter(name="Vendors").exists()

    if not is_vendor:
        return redirect("products:list")

    store = get_object_or_404(Store, id=store_id, vendor=request.user)

    if request.method == "POST":
        store.delete()
        return redirect("store_list")

    return render(request, "stores/delete_store.html", {"store": store})


def site_login(request):
    """Authenticate storefront users and block admin logins."""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_staff or user.is_superuser:
                messages.error(request, "Admins must log in through the admin panel.")
                return redirect("/admin/")

            login(request, user)
            return redirect("/products/")

        messages.error(request, "Invalid username or password.")

    return render(request, "registration/login.html")


def register(request):
    """Register a new buyer or vendor account."""

    if request.method == "POST":
        form = RegisterForm(request.POST)
        role = request.POST.get("role")

        if form.is_valid():
            user = form.save()
            user.email = form.cleaned_data["email"]
            user.save()

            Profile.objects.create(user=user, role=role)

            if role == "vendor":
                group, _ = Group.objects.get_or_create(name="Vendors")
                redirect_url = "store_list"
            else:
                group, _ = Group.objects.get_or_create(name="Buyers")
                redirect_url = "products:list"

            user.groups.add(group)

            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect(redirect_url)

    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})


# -------------------------
# Part 2 REST API Views
# -------------------------


@api_view(["GET"])
def list_stores(request):
    """Return a list of all stores as JSON."""

    stores = Store.objects.all()
    serializer = StoreSerializer(stores, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_store(request, store_id):
    """Return a single store by ID as JSON."""

    store = get_object_or_404(Store, pk=store_id)
    serializer = StoreSerializer(store)
    return Response(serializer.data)


@api_view(["GET"])
def vendor_stores(request, vendor_id):
    """Return all stores belonging to a specific vendor as JSON."""

    try:
        User.objects.get(pk=vendor_id)
    except User.DoesNotExist:
        return Response(
            {"detail": "Vendor not found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    stores = Store.objects.filter(vendor_id=vendor_id)
    serializer = StoreSerializer(stores, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_store_api(request):
    """
    Create a new store through the REST API.

    Only authenticated users in the Vendors group may create stores.
    """

    if not request.user.is_authenticated:
        return Response(
            {"detail": "Authentication required to create a store."},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    if not request.user.groups.filter(name="Vendors").exists():
        return Response(
            {"detail": "Only vendors can create stores."},
            status=status.HTTP_403_FORBIDDEN,
        )

    serializer = StoreSerializer(data=request.data)

    if serializer.is_valid():
        store = serializer.save(vendor=request.user)

        return Response(
            StoreSerializer(store).data,
            status=status.HTTP_201_CREATED,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)