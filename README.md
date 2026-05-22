# eCommerce Part 1 Project

## Overview

This project is a Django-based eCommerce application that supports both vendors and buyers. Vendors can create and manage stores and products, while buyers can browse products, add items to a cart, complete purchases, and leave reviews.

The application implements role-based access control, session-based cart management, invoice generation, email notifications, and verified purchase reviews.

---

## Features
### Database

The application uses MariaDB as the backend database for storing:

- User accounts
- Stores
- Products
- Orders
- Reviews

### User Authentication

- User registration
- User login
- User logout
- Role-based access control for buyers and vendors

### Vendor Features

Vendors can:

- Create stores
- Edit stores
- Delete stores
- View all stores they own
- Add products to their stores
- Edit products
- Delete products

Vendor-only navigation and store management features are restricted to users assigned to the Vendors group.

### Buyer Features

Buyers can:

- Browse available products
- View product details
- Add products to a shopping cart
- Manage a session-based cart
- Checkout purchased items
- Receive an invoice via email
- Leave product reviews

### Shopping Cart

The application uses Django sessions to maintain a user's cart while browsing.

Features include:

- Add products to cart
- View cart contents
- View order totals
- Checkout purchased items
- Automatic cart clearing after successful checkout

### Checkout and Invoicing

During checkout:

- An order is created
- Order items are recorded
- An invoice is generated
- An invoice email is sent to the buyer
- Purchased items are removed from the cart

### Product Reviews

Buyers can submit product reviews.

The application automatically identifies whether the buyer previously purchased the product and displays:

- Verified Purchase
- Unverified

This helps provide trustworthy product feedback.

---

## Technologies Used

- Python
- Django
- MariaDB
- HTML
- CSS
- Django Sessions
- Django Authentication System

---

## Running the Project
python manage.py migrate
python manage.py runserver

http://127.0.0.1:8000/

### Clone the Repository

```bash
git clone <repository-url>
cd ecommerce_part1_project