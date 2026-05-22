from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from .models import Product, Order, OrderItem, Review
from stores.models import Store

"""Views for the products application.

Handles product browsing, vendor product management,
shopping cart functionality, checkout processing,
and product reviews including verified review detection."""


@login_required
def list_store_products(request, store_id):
    store = get_object_or_404(Store, id=store_id, vendor=request.user)
    products = Product.objects.filter(store=store)

    return render(
        request,
        "products/list_store_products.html",
        {"store": store, "products": products},
    )


@login_required
def add_product(request, store_id):
    store = get_object_or_404(Store, id=store_id, vendor=request.user)

    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        price = request.POST["price"]
        image = request.FILES.get("image")

        Product.objects.create(
            store=store, name=name, description=description, price=price, image=image
        )

        return redirect("products:list_store_products", store_id=store.id)

    return render(request, "products/add_product.html", {"store": store})


@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, store__vendor=request.user)

    if request.method == "POST":
        product.name = request.POST["name"]
        product.description = request.POST["description"]
        product.price = request.POST["price"]

        if "image" in request.FILES:
            product.image = request.FILES["image"]

        product.save()

        return redirect("products:list_store_products", store_id=product.store.id)

    return render(request, "products/edit_product.html", {"product": product})


@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, store__vendor=request.user)
    store_id = product.store.id
    product.delete()

    return redirect("products:list_store_products", store_id=store_id)


def add_to_cart(request, product_id):
    """Add a product to the user's cart.

    Stores cart data in session and redirects back to the cart or product page.
    """

    cart = request.session.get("cart", {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session["cart"] = cart

    return redirect("products:cart_view")


def cart_view(request):
    cart = request.session.get("cart", {})
    products = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        product.quantity = quantity
        product.total_price = product.price * quantity
        total += product.total_price
        products.append(product)

    return render(request, "cart/cart.html", {"products": products, "total": total})


@login_required
def checkout(request):
    """Processes the user's cart, creates an order, sends an invoice email,
    and clears the session cart."""
    cart = request.session.get("cart", {})

    if not cart:
        return redirect("products:cart_view")

    order = Order.objects.create(buyer=request.user)
    total = 0
    invoice_lines = []

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)

        OrderItem.objects.create(order=order, product=product, quantity=quantity)

        line_total = product.price * quantity
        total += line_total
        invoice_lines.append(f"{product.name} x {quantity} = {line_total}")

    invoice_message = (
        f"Thank you for your purchase!\n\n"
        f"Order #{order.id}\n\n" + "\n".join(invoice_lines) + f"\n\nTotal: {total}"
    )

    if request.user.email:
        send_mail(
            "Your Order Invoice",
            invoice_message,
            "store@example.com",
            [request.user.email],
            fail_silently=True,
        )

    request.session["cart"] = {}

    return render(request, "checkout_success.html", {"order": order, "total": total})


def browse_products(request):
    """Display the buyer-facing product listing page.

    Shows available products and provides entry points for login/registration.
    Vendors are also shown a link to manage their stores.
    """

    products = Product.objects.select_related("store").all()

    is_vendor = (
        request.user.is_authenticated
        and request.user.groups.filter(name="Vendors").exists()
    )

    return render(
        request,
        "products/browse_products.html",
        {
            "products": products,
            "is_vendor": is_vendor,
        },
    )


def product_detail(request, product_id):
    """Display a single product detail page including reviews.

    Loads product information and associated reviews for display.
    """

    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all().order_by("-created_at")

    return render(
        request,
        "products/product_detail.html",
        {"product": product, "reviews": reviews},
    )


@login_required
def leave_review(request, product_id):
    """Allow a logged-in buyer to submit a review for a product.

    Creates a review associated with request.user and the selected product.
    """

    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        rating = request.POST["rating"]
        comment = request.POST["comment"]

        # This code makes the review verified or unverified.
        purchased = OrderItem.objects.filter(
            order__buyer=request.user, product=product
        ).exists()

        Review.objects.create(
            product=product,
            user=request.user,
            rating=rating,
            comment=comment,
            verified=purchased,
        )

        return redirect("products:product_detail", product_id=product.id)

    return render(request, "products/leave_review.html", {"product": product})
