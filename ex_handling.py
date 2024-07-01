def sqrrt():
    try:
        num = float(input("Enter a number: "))
        square_root = num ** 0.5
        print(f"The square root of {num} is {square_root}")
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
        sqrrt()
    
sqrrt()
