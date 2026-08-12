cheese_pizza = 10.00
pepperoni= 1.50
cheese = 1.50
mushrooms = 1.50

def calculate_total(topping_count):
    total = cheese_pizza + (topping_count * (pepperoni + cheese + mushrooms))
    return total

while True:
        topping_count = int(input("How many toppings would you like to add? "))
        if topping_count < 0:
            print("Please enter a non-negative number.")
            continue
        total_price = calculate_total(topping_count)
        print("Your total price is: ${total_price:}")
        break
    