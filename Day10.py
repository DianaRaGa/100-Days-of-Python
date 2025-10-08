from Modules.Day10_Calc import logo

def add(n1, n2):
    return n1 + n2

# To do: Write out the other 3 functions - subtract, multiply and divide

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return  n1 * n2

def divide(n1, n2):
    return n1 / n2

# To Do: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# To DO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
def operaciones_inicio():
    print(logo)
    number_1 = int(input("Please enter the first number: "))
    for symbols in operations:
        print((symbols))
    operator = input("What operations are you wishing to do? ")
    number_2 = int(input("Please enter the second number of the operations: "))
    result = operations[operator](number_1, number_2)
    print(f"{number_1} {operator} {number_2} = {result}")
    return result

def operaciones_regreso(n1):
    for symbols in operations:
        print((symbols))
    operator = input("What operations are you wishing to do? ")
    number_2 = int(input("Please enter the second number of the operations "))
    result = operations[operator](n1, number_2)
    print(f"{n_1} {operator} {number_2} = {result}")
    return result

continue_the_code = "r"
item = True
while item:
    if continue_the_code == "r":
        print("\n" * 20)
        n_1 = operaciones_inicio()

    elif continue_the_code == "y":
        n_1 = operaciones_regreso(n_1)

    else:
        print("You chose to finish the program. Thank you!")
        quit()
    continue_the_code = input("You wish to continue with the result from the previews calculation (y), restart te program (r) or quit (q)?")
