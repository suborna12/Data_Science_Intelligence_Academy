while True:
    try:
        age = int(input("Enter your age: "))
        print(f"You are {age} years old")
        break 
        
    except ValueError:
           print("Numbers only")