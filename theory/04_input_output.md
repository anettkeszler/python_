# User Input, Console Output

- **input() function** is designed to get data from the user
- input() takes a single parameter that is a string (often called **prompt**)
```python
email = input('Please enter your email address: ')
print(email) # prompted answer is printed
```
- It is important to note that the value returned from the input function will be a **string** representing the exact characters that were entered after the prompt.
- If you want this string interpreted as another type, you must provide the **type conversion explicitly**. <br><br>
- **print() function** is used to outputs in Python
- print() displays their parameters using a single blank as the default separator
- to change the default separator character, set the ```sep``` argument
- each print ends with a newline character by default, to change this, set the ```end``` argument
```python
print("Hello", "World!", sep ="***") # Hello***World!
print("Hello", "World", end="***") # Hello World***
```

### String formatting 
```python
a = 10
b = 5
result = a + b
print('Adding the value of {} and {} = {}'.format(a, b, result))  # direct formatting 
```
```python
# STRING FORMATTING

str1 = input('Please enter your first name: ')
str2 = input('Please enter your second name: ')

# concatenation
print('Hello, ' + str1 + ' ' + str2)

# direct formatting
print("Hello, {} {}".format(str1, str2))

num_1 = input('First number is: ')
num_2 = input('Second number is: ')
result = float(num_1) + float(num_2)

# concatenation:
print("The sum of: " + num_1 + " and " + num_2 + " is " + str(result))

# direct formatting:
print("The sum of {} and {} is {}".format(num1, num2, result))
```

#### DIRECT FORMATTING
- you can control the order by specifying the numbers inside the curly brackets 
```python
print("I like {0} more than {1}.".format("oranges", "grapes"))
# I like oranges more than grapes.

print("I like {1} more than {0}.".format("oranges", "grapes"))
# I like grapes more than oranges.
```