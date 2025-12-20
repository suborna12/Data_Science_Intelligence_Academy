<h1><strong>Day 6 Functions Modularity</strong></h1>
<h3><strong>DEEP DIVE: Theory: The Stack Scope</strong></h3>
When a function is called, Python creates a "Stack Frame" in memory. All variables created inside the function live there. When the function returns, the frame is destroyed. LEGB Rule: Python searches for variables in this order: Local -> Enclosing -> Global -> Built-in.

```
def calculate_area(radius: float) -> float: 
"""Returns area of circle. Inputs float.""" 
    if radius < 0:
        return 0 
    return 3.14 * (radius **2)

# Main Execution  
r = 5 
print (calculate_area (r))
```

# Goals:
1.Understand that assigning a variable inside a function creates a local variable and does not change the global one.

2.Learn that a function returns None if no return statement is used, even if it prints a value.

3.Understand that default arguments are stored when the function is defined and used if no value is passed.

4.Learn that comparison expressions directly return Boolean values and can be returned without if/else.
