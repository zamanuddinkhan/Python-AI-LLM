'''
Build a Product store which satisfy the following:
1. Design & create an online store for Products (name, price).

2. Track total products being created.

3. Create a static method to calculate discount on each product based on a % parameter.
'''

class Product:
    count = 0

    def __init__(self, name, price):
        self.store(name, price)
        Product.count += 1

    def get_info(self):  # Instance method
        print(f"Price of {self.name} is Rs. {self.price}")

    def store(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def get_count(cls):
        print(f"Total products in store = {cls.count}")

    @staticmethod
    def get_discount(price, discount):
        final_price = price - (price * discount) / 100
        print(f"Final price after discount = Rs. {final_price}")


# Creating products
p1 = Product("Phone", 10_000)
p2 = Product("Laptop", 100_000)
p3 = Product("Computer", 70_000)

products = [p1, p2, p3]

# Display product information
for product in products:
    product.get_info()

# Display total products
Product.get_count()

# Calculate discount on each product
for product in products:
    Product.get_discount(product.price, 10)