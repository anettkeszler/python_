# Variables and Functions & Type Casting

### Variables
- To create a variable you need to declare a name and assign it a value  
- To change the value of a variable that has already been declared, you only need to reassign or redeclare it 
- In general, the right-hand side of the assignment statement is evaluated and a reference to the resulting data object is assigned to the name on the left-hand side
- **Naming conventions**:
    - **camelCase**: first letter is lowercase, and the first letter of every world after is uppercase with no space between words (myFirstName) 
    - **snake_case**: everything is lowercase, but use an underscore between words (my_first_name)
- When creating a variable, python automatically assigns the datatype for you
```python
name = "Leo"    # String
age = 7         # Integer
height = 5.6    # Float
is_cat = True   # Boolean
flaws = None    # None type
```
- You can declare multiple variables and assignt them to the same value (**parallel assignment**): <br>
``` a = b = c = 10```
- You can declare multiple variables and assign them to multiple values (**chained assignment**):<br>
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
    - similar terms in other languages: type inference, type coercion, type casting
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
```python
print(10 == 10)     # True
print(10 == 10.0)   # True - implicit type conversion - int and float

# when Python runs operations involving integers and floats, it implicitly converts the integers type to a float
print(10 + 10.0)    # 20.0 

print(type(10 + 10.0)) # <class 'float'> , implicit type conversion
```

### VARIABLE SCOPES
- built-in
- global
- local
- enclosed

```python
global_variable = 10

def func_1():
    enclosed_variable = 8
    def func_2():
    
        local_variable = 5
        print(f"Access to global variable: {global_variable}")
        print(f"Access to eclosed variable: {enclosed_variable}")

    func_2()

print(func_1())


# animalfarm
print("Animalfarm:")
def d():
    animal = "elephant"
    def e():
        nonlocal animal
        animal = "giraffe"
        print(f"Inside nested function: {animal}")

    print(f"Before calling function: {animal}")
    e()
    print(f"After nested function: {animal}")

animal = "camel"
d()
print(f"Global animal: {animal}")

# The nonlocal keyword is used to work with variables inside nested functions, 
# where the variable should not belong to the inner function.
```