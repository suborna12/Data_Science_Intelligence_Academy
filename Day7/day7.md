# Day 7 Error Handling(Exceptions)
<h3><b>DEEP DIVE: Theory: Exception Bubbling</b></h3>
When an error occurs, it"bubbles up" the call stack. If nothing catches it, the program crashes.
Defensive Programming: We use try/except blocks to catch these bubbles. This is required for Data Science pipelines where one bad row of data shouldn't stop a 10-hour training process.

```
while True: 
    try: 
        val = int(input("Enter number: ")) 
        print (100 / val) 
        break 
    except ValueError: 
        print("Text is not allowed.") 
    except ZeroDivisionError:  
        print ("Cannot divide by zero.") 
```

<h3><b>Goals:</b></h3>
1.Input Guard: The goal is to stop the program from crashing due to invalid user input by catching errors and showing a message. 
2.Math Safety Net: The goal is to handle division by zero safely so the program continues running. 
3.Cleanup Crew: The goal is to always run cleanup code, whether an error occurs or not. 
4.Custom Signal: The goal is to enforce rules by manually raising errors for invalid input.
