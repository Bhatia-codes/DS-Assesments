def calculator():
    while True:
        expression = input("Enter a mathematical expression (e.g. 2+2, 3*4, 1+2+3, etc.): ")

        if expression.lower() == "exit":
            break

        try:
            result = eval(expression)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {str(e)}")

calculator()