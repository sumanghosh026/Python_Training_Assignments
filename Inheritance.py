# <!-- Scenario:
 
# You are building the backend logic of a product and order management system for an e-commerce platform like Amazon or Flipkart. The system needs to handle products, users, payments, discounts, and different order behaviors dynamically.
 
# Q1. Product Search System (Static Polymorphism)
 
# Problem Statement:
# Implement a class ProductSearch that allows searching products with different combinations of criteria (name, category, price range).
 
# Requirements:
 
# Use default arguments and/or *args, **kwargs to simulate method overloading.
 
# Allow the following types of searches:
 
# Only by name
 
# Name and category
 
# Name, category, and price range
 
 
# Q2. Cart System with Quantity Variations (Static Polymorphism)
 
# Problem Statement:
# Design a class Cart that can add multiple products with variable quantities using *args or **kwargs.
 
# Requirements:
 
# Add multiple products at once with name and quantity
 
# Simulate static polymorphism using variable arguments
 
 
# Q3. Discount Application (Static Polymorphism)
 
# Problem Statement:
# Create a class Discount that allows applying different types of discounts:
 
# Flat discount
 
# Percentage discount
 
# Buy One Get One
 
# Use static polymorphism to overload the method using default parameters or *args
 
 
# Q4. Payment System (Dynamic Polymorphism)
 
# Problem Statement:
# Implement a base class Payment and subclasses CreditCardPayment, UPIPayment, and CODPayment. Each should override a method pay().
 
# Requirements:
 
# Override pay() method in each class to simulate different payment methods -->

class ProductSearch:
    def __init__(self, products):
        self.products = products  # List of dictionaries with product info

    def search(self, name=None, category=None, min_price=None, max_price=None):
        results = self.products

        if name:
            results = [p for p in results if p['name'].lower() == name.lower()]
        if category:
            results = [p for p in results if p['category'].lower() == category.lower()]
        if min_price is not None and max_price is not None:
            results = [p for p in results if min_price <= p['price'] <= max_price]

        return results

products = [
    {'name': 'Laptop', 'category': 'Electronics', 'price': 800},
    {'name': 'Shirt', 'category': 'Fashion', 'price': 30},
    {'name': 'Laptop', 'category': 'Electronics', 'price': 1000},
]

searcher = ProductSearch(products)

print("Search by name:")
print(searcher.search(name='Laptop'))

print("Search by name and category:")
print(searcher.search(name='Laptop', category='Electronics'))

print("Search by all:")
print(searcher.search(name='Laptop', category='Electronics', min_price=500, max_price=900))


class Cart:
    def __init__(self):
        self.items = {}  # {'product_name': quantity}

    def add_products(self, **kwargs):
        for product, qty in kwargs.items():
            if product in self.items:
                self.items[product] += qty
            else:
                self.items[product] = qty

    def show_cart(self):
        return self.items
cart = Cart()
cart.add_products(Laptop=1, Shirt=2, Mouse=3)
cart.add_products(Shirt=1, Keyboard=1)

print("Cart contents:")
print(cart.show_cart())


class Discount:
    def apply_discount(self, amount, discount_type='flat', value=0):
        if discount_type == 'flat':
            return max(amount - value, 0)
        elif discount_type == 'percentage':
            return max(amount - (amount * value / 100), 0)
        elif discount_type == 'bogo':  # Buy One Get One
            # Assuming value is the unit price of the product
            return amount - value
        else:
            raise ValueError("Unsupported discount type")

discount = Discount()

print("Flat discount:")
print(discount.apply_discount(1000, discount_type='flat', value=100))  # 900

print("Percentage discount:")
print(discount.apply_discount(1000, discount_type='percentage', value=10))  # 900

print("BOGO discount (assuming one item price = 500):")
print(discount.apply_discount(1000, discount_type='bogo', value=500))  # 500


class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement the pay() method.")

class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card."

class UPIPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using UPI."

class CODPayment(Payment):
    def pay(self, amount):
        return f"Payment of {amount} will be made on delivery (COD)."

payments = [
    CreditCardPayment(),
    UPIPayment(),
    CODPayment()
]

for method in payments:
    print(method.pay(500))
