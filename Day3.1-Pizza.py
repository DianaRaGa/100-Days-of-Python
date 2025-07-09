print("Welcome to Python Pizza Deliveries!")

#Setting up the variables
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
price = 0

# Checking the price for the size pizza
if size == "S":
    price += 15
    if pepperoni == "Y":
        price += 2
elif size == "M":
    price += 20
    if pepperoni == "Y":
        price += 3
else:
    price += 25
    if pepperoni == "Y":
        price += 3

# Checking for the extra cheese
if extra_cheese == "Y":
    price += 1

print(f"Your final bill is: ${price}.")
