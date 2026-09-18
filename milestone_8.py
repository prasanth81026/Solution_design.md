class Product:
    def __init__(self, name, price, quantity,stock):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.stock = stock 
    def product_calculation(self, price,quantity, stock):
        total_bill = 0
        if quantity < 0:
           print("select quantity greater than one")
        elif quantity > stock:
            print("out of stock")
        else:
            total_bill += quantity*price
            print(total_bill)

p = Product("rice", 1200,4,40)
p.product_calculation(40,-2,7)

