class Customer_hierarchy:
    
    def __init__(self, customer):
        self.customer = customer 
    def display_customer_discount(self):
        if self.customer == "Regular":
            discount = 0
            print(discount)
        elif self.customer == "Premium":
            discount = 20
            print(discount)
        else:
            discount = 40
            print(discount)
    def purchase_details(self, Purchase):
        self.Purchase = Purchase
        if self.Purchase <= 5000:
            print("You are my regular customer, Thanks for visiting us")
        elif self.Purchase > 5000 and self.Purchase <= 10000:
            print("You are my premium customer, Thanks for visiting us")
        else:
            print("You are my corporatecustomer, Thanks for visiting us")


customer_type = Customer_hierarchy(input("Enter the customer type: "))
customer_type.display_customer_discount()
customer_type.purchase_details(int(input("Enter the purchase amount: ")))
