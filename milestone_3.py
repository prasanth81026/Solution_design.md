class Customer_hierarchy:
    
    def __init__(self, customer):
        self.customer = customer 
    def display_customer_discount(self):
        if self.customer == "normal":
            discount = 0
            print(discount)
        elif self.customer == "Premium":
            discount = 20
            print(discount)
        else:
            discount = 40
            print(discount)


customer_type = Customer_hierarchy(input("Enter the customer type: "))
customer_type.display_customer_discount()
