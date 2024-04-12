"""
Suppose we have a Product class that represents a generic product, and we want to calculate the total price of a list of products. Initially, the Product class only has a price attribute, and we 
can calculate the total price of products based on their prices

Now, let's say we want to add a discount feature, where some products might have a discount applied to their prices. To add this feature, we would need to modify the existing Product class and the calculate_total_price function, which violates the Open/Closed Principle. Redesign this program to follow the Open-Closed Principle (OCP) which represents “Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.”
"""

class Product:
    def __init__(self, price):
        self.price = price

    def getPrice(self):
        return self.price 

class DiscountedProduct(Product):
    def getPrice(self):
        self.discount = 20
        # assuming the discount is in percentage 
        return super().getPrice() - (super().getPrice() * self.discount /100)

def calculate_total_price(products):
    total_price = 0
    for product in products:
        total_price += product.getPrice()
    return total_price

# Using the calculate_total_price function with a list of products
products = [Product(100), Product(50), Product(75), Product(300)]

products2 = [Product(100), Product(50), Product(75), DiscountedProduct(300)]

print("Total Price without Discount is :", calculate_total_price(products))

print("Total Price after discount is :", calculate_total_price(products2))


 