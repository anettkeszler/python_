# Exception Handling

- Usually there are 2 types of errors occure when writing programs:
1. **Syntax Error**: 
    - usually caused by the developer (misspelling/typo or indentation issues)
    - it has minimal impact, because most IDEs warn the developer and give ideas how to fix them 
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
    - when an exception occurs, we say that is has been ```raised```
    - you can handle the exceptionthat has been raised by using a ```try``` statement

```python
# ZeroDivisionError
def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("ZeroDivisionError,", e)
        print(e.__class__)
    except Exception as e:
        print("Something went wrong,", e)

result = divide_by(29, 0)
print(result)
```
```python
# FileNotFoundError
try:
    with open('file_not_exist.txt', 'r') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e.__class__)
    print("FileNotFoundError,", e)
```
```python
# IndexError
items = [1,2,3,4,5]

# item = items[6]
# print(item)     # IndexError: list index out of range

try:
    item = items[6]
    print(item)
except IndexError as e:
    print(e.__class__)
    print("IndexError,", e)
```


