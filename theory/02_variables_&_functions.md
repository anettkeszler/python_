# Variables and Functions & Type Casting

### Variables
- To create a variable you need to declare a name and assign it a value  
- To change the value of a variable that has already been declared, you only need to reassign or redeclare it 
- **Naming conventions**:
    - **camelCase**: first letter is lowercase, and the first letter of every world after is uppercase with no space between words (myFirstName) 
    - **snake_case**: everything is lowercase, but use an underscore between words (my_first_name)
- When creating a variable, python automatically assigns the datatype for you
```
name = "Leo"    # String
age = 7         # Integer
height = 5.6    # Float
is_cat = True   # Boolean
flaws = None    # None type
```
- You can declare multiple variables and assignt them to the same value (parallel assignment): <br>
``` a = b = c = 10```
- You can declare multiple variables and assign them to multiple values (chained assignment):<br>
```a, b, c = 1, 2, 3```
- You can delete a variable: <br>
```del x```

### Defining a function
- function can hide the details of any computation 
- function has a name, parameters and a body
- function returns a value

### Type Casting - data type conversion
- typecasting is the process of converting one data type to another 
- **implicit data type conversion**: 
    - is automatical by Python's compiler to prevent data loss (int --> float). 
    - it only works if the data types are compatible (int - float). 
- **explicit data type conversion**: when implicit conversion throws a type error (TypeError)
    - int('55') --> 55
    - str(45) --> '45', it converts **any data type** into a string datatype
    - float('20.45') --> 20.45
    - bool()
    - tuple()
    - list()
    - set()
    - dict() 
    - ord() --> returns an integer representing the underlying unicode character 
    - hex() --> converts a given integer to a hexadecimal string 
    - oct() --> takes an integer and returns a string representing an oct to a number  

  ![alt text](/screenshots/type_conversion.png)