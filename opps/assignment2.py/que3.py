
# An e-commerce company wants to calculate the final amount payable by customers after applying discounts.

# Requirements

# Create a class named Product with:

# product_id
# product_name
# quantity
# price_per_item

# Initialize the values using a constructor.

# Calculations
# Total Amount = Quantity × Price Per Item
# If Total Amount > ₹5000, Discount = 10%
# Otherwise, Discount = 5%
# Final Amount = Total Amount − Discount
# Sample Input
# Enter Product ID : P101
# Enter Product Name : Laptop
# Enter Quantity : 2
# Enter Price Per Item : 35000
# Sample Output
# ------ Shopping Bill ------
# Product ID        : P101
# Product Name      : Laptop
# Quantity          : 2
# Price Per Item    : 35000.0
# Total Amount      : ₹70000.0
# Discount          : ₹7000.0
# Final Amount      : ₹63000.0


class ecommerce:
    def __init__(self):
        self.productid=int(input("enter your product id"))
        self.productname=input("enter your product name")
        self.productquantity=int(input("enter your product quantity"))
        self.priceperitems=int(input("enter price per items"))
    def calculation(self):
        self.total=self.productquantity*self.priceperitems
        if self.total>5000:
            self.dis=self.total*20/100
        else:
            self.dis=self.total*5/100
    def finalamount(self):
        self.final=self.total-self.dis        
    def display(self):
        print("Product ID",self.productid)
        print("Product ID",self.productname)
        print("Product ID",self.productquantity)
        print("Product ID",self.priceperitems)
        print("Product ID",self.dis)
        print("Product ID",self.final)
obj1=ecommerce()
obj1.calculation()
obj1.finalamount()
obj1.display()
        