mars = 0.38
jupiter = 2.34
moon = 0.16

earth_weight= int(input("What is your weight(in kg)?"))
destination = str(input("Where is your destination?"))

def calculate_space_weight(earth_weight, destination):
    
    if destination == "Mars":
        return print("Your weight on Mars is:", earth_weight * mars)
    elif destination == "Jupiter":
        return print("Your weight on Jupiter is:", earth_weight * jupiter)
    elif destination == "Moon":
        return print("Your weight on Moon is:", earth_weight * moon)
    else: 
        return print("Invalid destination. Please enter Mars, Jupiter, or Moon.")

print(calculate_space_weight(earth_weight, destination))
    

   