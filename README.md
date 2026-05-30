# eComm2_Fixed/

## Repository
https://github.com/Tammied68/eCommerce_Part_2

## Overview

This project is a Django-based eCommerce application developed as part of the HyperionDev Software Engineering Bootcamp.

Part 2 extends the functionality implemented in Part 1 by integrating Django REST Framework (DRF) and exposing store and product data through RESTful API endpoints.

The application supports two user roles:

* **Buyers** who can browse products, add items to a shopping cart, complete purchases, and leave reviews.
* **Vendors** who can create stores and manage products within those stores.

The system implements role-based access control, session-based shopping carts, checkout functionality, invoice generation, email notifications, password recovery, verified purchase reviews, and REST API functionality.

---

## Features

### Authentication

The application includes:

* User registration
* User login
* User logout
* Password reset and account recovery
* Role-based access control
* Automatic buyer/vendor group assignment during registration

Users are automatically assigned to the appropriate Django group when registering, allowing immediate access to role-specific functionality.

---

### Vendor Features

Vendors can:

* Create stores
* Edit stores
* Delete stores
* View stores they own
* Add products to stores
* Edit products
* Delete products
* View customer reviews on products

Vendor-only functionality is protected through role-based permissions.

---

### Buyer Features

Buyers can:

* Browse available products
* View product details
* Add products to a shopping cart
* Checkout purchases
* Leave product reviews
* View verified purchase indicators

---

### Shopping Cart

The application uses Django sessions to maintain cart contents while users browse the store.

Features include:

* Add products to cart
* View cart contents
* View order totals
* Checkout purchased items
* Automatic cart clearing after successful checkout

---

### Checkout and Invoicing

When a buyer completes checkout:

* An order is created
* Order items are recorded
* Products are removed from the cart
* An invoice is generated
* An invoice email is sent to the buyer

---

### Product Reviews

Buyers can leave reviews on products.

The application automatically determines whether a user has previously purchased a product and displays:

* **Verified Purchase**
* **Unverified**

This provides more trustworthy feedback for future buyers.

---

### Account Recovery

The application implements Django's built-in password reset functionality.

Features include:

* Password reset request by email
* Secure password reset tokens
* Password reset confirmation page
* Password reset completion page

During development, password reset emails are displayed in the terminal using Django's Console Email Backend.

---

## REST API Functionality

Part 2 extends the application by providing RESTful API endpoints using Django REST Framework.

API functionality includes:

* Retrieve all stores
* Retrieve a single store
* Retrieve stores belonging to a vendor
* Create stores via API
* Retrieve products belonging to a store
* Create products via API

All API responses are returned in JSON format.

---

## API Endpoints

### Stores API

| Method | Endpoint                          | Description                               |
| ------ | --------------------------------- | ----------------------------------------- |
| GET    | `/stores/api/`                    | Retrieve all stores                       |
| GET    | `/stores/api/<store_id>/`         | Retrieve a single store                   |
| GET    | `/stores/api/vendor/<vendor_id>/` | Retrieve all stores belonging to a vendor |
| POST   | `/stores/api/create/`             | Create a new store                        |

### Products API

| Method | Endpoint                          | Description                      |
| ------ | --------------------------------- | -------------------------------- |
| GET    | `/products/api/store/<store_id>/` | Retrieve products for a store    |
| POST   | `/products/api/store/<store_id>/` | Create a new product for a store |

---

## Technologies Used

* Python
* Django
* Django REST Framework (DRF)
* SQLite
* HTML
* CSS
* Bootstrap
* Django Sessions
* Django Authentication System

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Tammied68/eCommerce_Part_2.git
cd eComm2_Fixed
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

This project uses MariaDB as the database backend.

Database configuration can be found in:

ecommerce_project/settings.py

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

Run the development server:

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
3. Browse available products.
4. View product details.
5. Add products to the cart.
6. Checkout purchases.
7. Leave reviews.
8. Submit verified purchase reviews after checkout.

---

### Vendor Workflow

1. Register a vendor account.
2. Log in.
3. Access **My Stores**.
4. Create a store.
5. Add products to the store.
6. Edit products.
7. Delete products.
8. Edit or delete stores.

---

## Project Structure

```text
ecommerce_part2_project/
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

### Part 1 Requirements

* User registration
* User login and logout
* Password reset functionality
* Vendor store management
* Product management
* Session-based shopping cart
* Checkout process
* Invoice generation
* Email notifications
* Product reviews
* Verified purchase reviews
* Role-based permissions
* Automatic buyer/vendor group assignment

### Part 2 Requirements

* Django REST Framework integration
* Store API endpoints
* Product API endpoints
* JSON API responses
* Vendor store retrieval API
* Store product retrieval API
* Authenticated API creation endpoints

---

## Testing

### Vendor Testing

Verified functionality includes:

* Vendor registration
* Vendor login
* Store creation
* Store editing
* Store deletion
* Product creation
* Product editing
* Product deletion

### Buyer Testing

Verified functionality includes:

* Buyer registration
* Buyer login
* Product browsing
* Cart management
* Checkout process
* Product reviews
* Verified purchase reviews

### API Testing

Verified functionality includes:

* Retrieve all stores
* Retrieve a single store
* Retrieve vendor stores
* Create stores through API
* Retrieve store products
* Create products through API

---

## Author

**Tammie Davis**
University of Chicago, HyperionDev Software Engineering Bootcamp
