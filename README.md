# eCommerce Application Part 1

## Overview

This project is a Django-based eCommerce application developed as part of the HyperionDev Software Engineering Bootcamp.

The application supports two user roles:

* **Buyers** who can browse products, add items to a shopping cart, complete purchases, and leave reviews.
* **Vendors** who can create stores and manage products within those stores.

The system implements role-based access control, session-based cart management, checkout functionality, invoice generation, email notifications, and verified purchase reviews.

---

## Features

### Authentication

* User registration
* User login
* User logout
* Role-based access control

### Vendor Features

Vendors can:

* Create stores
* Edit stores
* Delete stores
* View stores they own
* Add products
* Edit products
* Delete products

### Buyer Features

Buyers can:

* Browse products
* View product details
* Add products to a shopping cart
* Checkout purchases
* Leave reviews
* View verified purchase indicators

### Shopping Cart

The application uses Django sessions to maintain cart contents while users browse the store.

### Checkout and Invoicing

When a buyer completes checkout:

* An order is created
* Products are removed from the cart
* An invoice is generated
* An invoice email is sent to the buyer

### Product Reviews

Buyers can submit product reviews.

The application automatically identifies verified purchases and displays:

* Verified Purchase
* Unverified

based on whether the buyer previously purchased the product.

---

## Technologies Used

* Python
* Django
* MariaDB
* HTML
* CSS
* Django Sessions
* Django Authentication System

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Tammied68/ecommerce_part1_project-.git
cd ecommerce_part1_project
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

macOS/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Database Configuration

This project uses MariaDB.

Update the database settings in:

```text
ecommerce_project/settings.py
```

Example configuration:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "ecommerce_db",
        "USER": "your_username",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

---

## Running the Application

Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## Application Workflow

### Buyer Workflow

1. Register a buyer account.
2. Log in.
3. Browse products.
4. Add products to the cart.
5. Checkout.
6. Leave a review.

### Vendor Workflow

1. Register a vendor account.
2. Log in.
3. Select **My Stores**.
4. Create a store.
5. Add products to the store.
6. Edit or delete stores and products.

---

## Project Structure

```text
ecommerce_part1_project/
│
├── ecommerce_project/
├── stores/
├── products/
├── templates/
├── static/
├── manage.py
└── requirements.txt
```

---

## Assignment Requirements Implemented

* User registration and authentication
* Vendor store management
* Product management
* Session-based shopping cart
* Checkout process
* Invoice generation
* Email notifications
* Product reviews
* Verified purchase reviews
* Role-based permissions
* MariaDB database integration

---

## Author

**Tammie Davis**
University of Chicago
HyperionDev Software Engineering Bootcamp

---