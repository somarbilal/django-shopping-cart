# django-shopping-cart
Stripe payment processing platform to handle payments for purchases.


# Installation

Clone the repository

Create a virtual environment and activate it

Install the requirements from requirements.txt

Set up the database

Run the development server

# Usage
The main functionality of the project is to display a product on a landing page and allow customers to purchase it. The project integrates with Stripe to handle payments.

# Models
The Product model represents a single product in the store. It has the following fields:

name: the name of the product

description: a longer description of the product

price: the price of the product in cents

The model also has a get_display_price method that returns the price of the product in dollars and cents.

# Views
There are four views in the project:

ProductLandingPageView: displays the landing page for the product 

CreateCheckoutSessionView: creates a checkout session with Stripe and returns the session ID

SuccessView: displays a success page after a successful payment

CancelView: displays a cancellation page if the customer cancels the payment process
