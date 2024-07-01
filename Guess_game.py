
def guess_the_number():
    print("Welcome to Guess the Number!")
    print("Think of a number between 1 and 100.")

    low = 1
    high = 100

    while True:
        
        mid = (low + high) // 2

        print(f"Number is {mid}?")

        response = input("Enter 'h' if the number is higher, 'l' if it's lower, or 'c' if I'm correct: ")

        if response == 'h':
            low = mid + 1
        elif response == 'l':
            high = mid - 1
        elif response == 'c':
            print("Yay! I guessed it!")
            break
        else:
            print("Invalid response. Please try again.")


guess_the_number()
