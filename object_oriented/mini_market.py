class RegularCustomer():
    def __init__(self, name, item, price, quantity):
        self.name = name
        self.item = item

        if price < 0:
            self.price = 1
        else:
            self.price = price

        if quantity < 0:
            self.quantity = 1
        else:
            self.quantity = quantity

    def discount(self):
        return self.price * 0.2

    def display(self):
        print("Customer: " + self.name + " bought " + str(self.quantity) + " " + self.item + " at " + str(self.price) + " each")



class OccasionalCustomer(RegularCustomer):
    def discount(self):
        return self.price * 0.08

    def display(self):
        print("Customer: " + self.name + " bought " + str(self.quantity) + " " + self.item + " at " + str(self.price) + " each")


customer1 = RegularCustomer("Makis" , "Milk" , 1.8 , 1)
customer2 = OccasionalCustomer("Giannis" , "Milk" , 1.8 , 1)

customer1.display()
print ("Discount: " + str(customer1.discount()) + " euro per item \nTotal: " + str(customer1.discount() * customer1.quantity) + " euro \nTotal with discount: " + str(customer1.price * customer1.quantity - customer1.discount() * customer1.quantity) + " euro \n  ")
customer2.display()
print ("Discount: " + str(customer2.discount()) + " euro per item \nTotal: " + str(customer2.discount() * customer2.quantity) + " euro \nTotal with discount: " + str(customer2.price * customer2.quantity - customer2.discount() * customer2.quantity) + " euro \n  ")

customer3 = RegularCustomer("Monkey" , "Banana" , -4 , -2)
customer3.display()
