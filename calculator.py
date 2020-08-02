# Program make a simple calculator

# This function adds two numbers
def addition(x, y):
    return x + y

# This function subtracts two numbers
def subtraction(x, y):
    return x - y

# This function multiplies two numbers
def multiplication(x, y):
    return x * y

# This function divides two numbers
def division(x, y):
    return x / y


print("choose operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        a = float(input("Enter a number: "))
        b = float(input("Enter another number: "))

        if choice == '1':
            print(a, "+", b, "=", addition(a, b))

        elif choice == '2':
            print(a, "-", b, "=", subtraction(a, b))

        elif choice == '3':
            print(a, "*", b, "=", multiplication(a, b))

        elif choice == '4':
            print(a, "/", b, "=", division(a, b))
        break
    else:
        print("Invalid Input")
