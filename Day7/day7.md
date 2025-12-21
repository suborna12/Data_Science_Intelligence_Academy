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
