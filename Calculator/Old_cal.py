def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    while True:
        choice = input("Enter your choice: ")

        if choice == "5":
            print("Goodbye!")
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == "1":
            result = add(num1, num2)
            print(result)
        elif choice == "2":
            result = sub(num1, num2)
            print(result)
        elif choice == "3":
            result = mul(num1, num2)
            print(result)
        elif choice == "4":
            result = div(num1, num2)
            print(result)
        else:
            print("Invalid choice. Please try again.")

calculator()