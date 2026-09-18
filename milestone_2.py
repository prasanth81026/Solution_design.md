class Product:
    def __init__(self, name, price, deal_price, quantity):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.quantity = quantity
        self.you_save = price - deal_price

    def display_product_details(self):
        print(self.price)
        print(self.deal_price)
        print(self.you_save)
    def add_product(self, name, quantity, deal_price):
        self.name = name
        self.quantity= quantity
        self.deal_price = deal_price
        total_price = deal_price * quantity
        print(total_price)
items = Product("Shirt", 1000, 800, 2)
items.display_product_details()

items.add_product("TV", 2, 20000)