<h1><strong>Day 6 Functions Modularity</strong></h1>
<h3><strong>DEEP DIVE: Theory: The Stack Scope</strong></h3>
When a function is called, Python creates a "Stack Frame" in memory. All variables created inside the function live there. When the function returns, the frame is destroyed. LEGB Rule: Python searches for variables in this order: Local -> Enclosing -> Global -> Built-in.

```
def calculate_area(radius: float) -> float: 
"""Returns area of circle. Inputs float.""" 
    if radius < 0:
        return 0 
    return 3.14 * (radius **2)
``` 

# Main Execution  
r = 5 
print (calculate_area (r)) 
Goals:
Local vs. Global Scope: When inside a function a variable is changes,Python creates a new local variable inside the function's stack frame. It does NOT touch the global. To modify the global, you would need the global keyword (but avoid this in production!).
Every Python function returns something. If you do not explicitly write return value, Python implicitly executes return None.
Default Arguments: In python if the caller provides no argument in function, Python grabs the stored default. This allows for flexible APIs where common settings are optional.
Learn logical comparisons in python which already produce True or False without using if/else.
