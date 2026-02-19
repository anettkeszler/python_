# Exception Handling

- Usually there are 2 types of errors occure when writign programs:

1. **Syntax Error**: 
    - usually caused by the developer (misspelling/typo or indentation issues)
    - it has minimal impact, because most IDEs warns the developer and gives ideas how to fix them 
    - Python interpreter cannot process
2. **Exception Error**: 
    - an error during execution/runtime causes an exception  
    - exceptions need to be handled by the developer
    - **Common exceptions**:
        - ZeroDivisionError: you try to divide a number by zero
        - ValueError: invalid value
        - TypeError: wrong type
        - IndexError: list index out of range, you try to access an item on an index which is out of range
        - KeyError: dictionary key not found
        - FileNotFoundError: file doesn't exist on the given place
    - in these cases the logic error leads to runtime error that causes the program to terminate --> Exceptions 

    