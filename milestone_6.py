class Product:
    def __init__(self, name, price, deal_price, rating):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.you_save = price - deal_price
        self.rating = rating
    def display_product_details(self):
        print(self.deal_price)
        print(self.you_save)
class customer(Product):
    def __init__(self,name,price,deal_price, rating,discount):
        super().__init__(self,name,price,deal_price, rating, discount)
        self.discount = discount 
    def discount_of_product(self,price):
        if price > 17000:
            self.discount = 20
            print(self.discount)
        else:
            self.discount = "buy more to get discount"
            print(self.discount)

class order(Product):
    def __init__(self,name,price,deal_price, rating, discount, quantity, my_orders):
        super().__init__(self,quantity,my_orders)
        self.quantity = quantity
        self.my_orders = my_orders
        my_orders = []
    def add_to_cart(self):
        total_price = quantity*self.deal_price
        my_orders.append(name,total_price)
        print(my_orders)
        
p = Product("laptop",67000,58000,4)
p.display_product_details()
c = customer("laptop",67000,58000,4.5,20)
c.discount_of_product(20000)

