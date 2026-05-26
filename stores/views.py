"""
Views for the stores application.

Provides functionality for vendors to create, edit, view, and delete stores,
and allows new users to register.
"""

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404, redirect, render
from .models import Profile, Store

# -------------------------
# Store Views (Vendor Only)
# -------------------------


@login_required
def store_list(request):
    """Display stores owned by the logged-in vendor.

    Users in the Vendors group can access this vendor dashboard.
    Non-vendor users are redirected to the buyer-facing product page.
    """

    is_vendor = request.user.groups.filter(name="Vendors").exists()

    if not is_vendor:
        return redirect("products:list")

    stores = Store.objects.filter(vendor=request.user)

    return render(
        request,
        "stores/store_list.html",
        {"stores": stores},
    )


@login_required
def create_store(request):
    """Allow vendors to create a new store."""

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
    """Edit an existing store owned by the logged-in vendor.

    Only the owner vendor can access this view; other users will receive a 404.
    """

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
    """Delete an existing store owned by the logged-in vendor.

    Confirms deletion via GET and removes the store via POST.
    """

    is_vendor = request.user.groups.filter(name="Vendors").exists()

    if not is_vendor:
        return redirect("products:list")

    store = get_object_or_404(Store, id=store_id, vendor=request.user)

    if request.method == "POST":
        store.delete()
        return redirect("store_list")

    return render(request, "stores/delete_store.html", {"store": store})


# -------------------------
# Authentication Views
# -------------------------


def site_login(request):
    """Authenticate storefront users (buyers/vendors) and block admin logins.

    Admin/staff users are redirected to the Django admin login page.
    Successful logins redirect to the buyer-facing product browsing page.
    """

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Admins must use Django admin
            if user.is_staff or user.is_superuser:
                messages.error(request, "Admins must log in through the admin panel.")
                return redirect("/admin/")

            login(request, user)
            return redirect("/products/")

        messages.error(request, "Invalid username or password.")

    return render(request, "registration/login.html")


def register(request):
    """Register a new buyer or vendor account.

    Creates the user's profile, assigns the correct Django group, logs the
    user in, and redirects them to the correct area of the application.
    """

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
