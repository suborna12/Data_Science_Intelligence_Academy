while True:
    try:
        x = int(input("Enter a number: "))
        print(f"The Resul is: {100/x}")
        break
    except ValueError:
        print("Text is not allowed")
    except ZeroDivisionError:
        print("Cannot divided by zero")