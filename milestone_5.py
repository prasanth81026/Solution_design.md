class order:
    
    def __init__(self, order_id, customer_name, items):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items  # List of items in the order

    def calculate_total(self):
        total = sum(item['price'] * item['quantity'] for item in self.items)
        return total

    def display_order(self):
        print(f"Order ID: {self.order_id}")
        print(f"Customer Name: {self.customer_name}")
        print("Items:")
        for item in self.items:
            print(f" - {item['name']} (Quantity: {item['quantity']}, Price: {item['price']})")
        print(f"Total: {self.calculate_total()}")
order_details = order(20, "John Doe", [{"name": "Laptop", "quantity": 1, "price": 1000}, {"name": "Mouse", "quantity": 2, "price": 25}])
order_details.display_order()
