# ecommerce-api

This is a Django-based backend API for an e-commerce platform. The API supports user authentication, product management, cart management, and order management. This project was built to handle core functionalities necessary for a scalable and robust e-commerce environment.

## Features

- **User Authentication**: Sign up and sign in functionality with password hashing and session management.
- **Product Management**: CRUD operations for products including adding, updating, and deleting products.
- **Cart Management**: Add products to cart, update quantities, and view cart details.
- **Order Management**: Place orders, view all orders, and filter orders by customer.

## Getting Started

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/greatwhite9/ecommerce-api.git
   cd ecommerce-api
   ```

2. **Set up a virtual environment:**

   It's recommended to use a virtual environment to manage dependencies. You can set up a virtual environment using `virtualenv`:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**

   Install the necessary Python packages listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   Migrate the database schema:

   ```bash
   python manage.py migrate
   ```

5. **Run the server:**

   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

6. **Access the API:**

   Once the server is running, you can access the API at `http://127.0.0.1:8000/`.

## API Endpoints

### Authentication

- **Sign Up**: `POST /signup`
- **Sign In**: `POST /signin`

### Product Management

- **Add Product**: `POST /addproduct`
- **Update Product**: `PUT /updateproduct/:productId`
- **Delete Product**: `DELETE /deleteproduct/:productId`
- **Get All Products**: `GET /products`

### Cart Management

- **Add Product to Cart**: `POST /cart/add`
- **Update Cart**: `PUT /cart/update`
- **Delete Product from Cart**: `DELETE /cart/delete`
- **Get Cart**: `GET /cart`

### Order Management

- **Place Order**: `POST /placeorder`
- **Get All Orders**: `GET /getallorders`
- **Get Orders by Customer ID**: `GET /orders/customer/{customerId}`
