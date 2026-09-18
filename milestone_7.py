class Product:
    def __init__(self, name, price, quantity,stock):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.stock = stock 
    def product_calculation(self, price,quantity, stock):
        total_bill = 0
        if quantity <= stock:
            total_bill += quantity*price
        print(total_bill)

p = Product("rice", 1200, 3, 40)
p.product_calculation(40,5,7)

