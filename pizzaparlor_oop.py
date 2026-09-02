from diagnostic2_mg_cagape import calculate_total

topping_count = int(input("How many toppings would you like to add? "))
cheese_pizza = 10.00
pepperoni= 1.50
cheese = 1.50
mushrooms = 1.50

class Pizza:

    def __init__(self, name, topping):
        self.name = name
        self.topping = topping
        self.total_price = cheese_pizza + (topping_count * 1.50)

    def display_info(self):
        print("Buyer Name: ", self.name)
        print("Chosen Topping/s: ", self.topping)
        print("Total Price:" , self.total_price)

    def display_status(self):
        if self.total_price < 10:
            return "Invalid order. Please add at least one topping."
        else:
            return "Order successful. Enjoy your pizza!"

buyer = Pizza("Julia", "Cheese, Pepperoni")

buyer.display_info()
print("------------------------------")

buyer.display_status()

