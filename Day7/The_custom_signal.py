try:
    user_input = int(input("Enter a number: "))
    if user_input < 0:
        raise ValueError("No negatives")
except :
    print("Error: Entered negative number")