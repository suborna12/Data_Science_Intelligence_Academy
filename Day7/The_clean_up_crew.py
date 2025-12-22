try:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    print(f"After divided first number by second number the result: {num1 / num2}")

except ZeroDivisionError:
    print("Cannot divided by zero")
finally:

    print("Execusion complete")
