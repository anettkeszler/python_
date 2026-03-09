# Control Flows

### Control flows
- Control flow refers to the order in which the instructions in a program are executed 
- **Control flows can be**:
    - **Conditional** (statements): **if, else, else if (elif)**
    - **Loops**: **for loop, while loop** 

## LOOPS
- Looping is used to iterate through the sequence and access each item inside the sequence
### WHILE LOOP 
- based upon a condition being true. Once the condition is no longer true the loop stops. 
- need the set up a condition, than a counter and set the count to 0
- the loop will run while the count is less than the length of the list 
- I have to increment the count by 1 at the end of the block, if not, it will end up in an infinite loop (keep looping until the compiler stops it from running out of memory)

```python
count = 0
while count < len(favorites):
    print("I like this dessert", favorites[count])
    count += 1 
```

### FOR LOOP:
- The for loop is based on the size or length of the elements to iterate over. 

```python
str = "Looping"

for char in str:
    print(char)

for i in range(10):
    print(i)


favorites = ["Banana", "Tiramisu", "Creme Brulee", "Chocolate cake"]

for item in favorites:
    print("I like this dessert:" , item)
```
- in a standard for loop, I don't have access to the index, but I can use the enumerate() function to do that:
```python
favorites = ['Banana', 'Apple', 'Tiramisu', 'Cake']

# enumerate() - to access the index in a for loop
for idx, item in enumerate(favorites):
    print(idx, item)
```

### Control statements:
- So far you looped over sequences based on the length of the data you wanted to iterate over 
- But in many cases, not necessary to iterate over the whole sequence, and you can control the flow of the loop and exit when a specific condition is met
- Control statements: **break, continue, pass**
    - **break**: will exit the loop when the given condition is met
    - **continue**: allows you to skip over a section of the loop but then continue on with the rest
    - **pass**: acts as a placeholder, allowing you to include an empty block of code without causing a syntax error. It does nothing and allows the program to continue execution normally.

```python
favorites = ["Banana", "Tiramisu", "Apple", "Chocolate cake"]

# 'break' will exit the loop when the given condition is met
for dessert in favorites:
    if dessert == "Apple":
        print(f"This is my favorite dessert: {dessert}")
        break       
else:
    print("Not a dessert on my list.")
    
# 'continue' allows you to skip over a section of the loop but then continue on with the rest
for dessert in favorites:
    if dessert == "Tiramisu":
        continue
    print(f"Other dessert I like: {dessert}")

# 'pass' - placeholder, it does nothing and allows the program to continue execution normally
for dessert in favorites:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert) 


for i in range(10):
    if i == 3:
        continue # Skip this iteration
    if i == 7:
        break # Exit loop
    print(i)
```

### Math and Logical operators
Operations in Python can be:
1. **Mathematical / Arithmetic Operators**: 
    - addition: +
    - subtraction: -
    - division: / 
    - multiplication: * 

```python
print(10 / 3)   # 3.3333333
print(1243 // 10)  # 124
print(1243 % 10)   # 3
print( 2 ** 3)  # 8 (2 * 2 * 2)

# USEFUL FUNCTIONS
print(abs(-5))              # 5
print(round(3.7))           # 4
print(round(3.14159, 2))    # 3.14
print(min(3, 4, 2, 6, 8))   # 2
print(max(1, 4, 6, 9, 2))   # 9
print(sum([1, 3, 5]))       # 9
```
2. **Logical Operators**: <br>
They used in **conditional statements** to determine a True or False outcome
    - and: checks for all conditions to be true 
    - or: checks for at least one conditions to be true 
    - not: return false if the result is true 

```python
a = True
b = True

if a and b:
    print("All True!")

a = True
b = False

if a or b:
    print("At least one is True")

a = True
b = False

if not(a) or not(b):
    print("All true!")
```

3. **Comparison Operators**:
```
x == y      # equal to
x!= y       # not equal to
x < y       # less than
x =< y      # less than or equal to
x > y       # greater than
x => y      # greater than or equal to
```

#### Match statement 
- compares a value to several different conditions until one of these conditions is met 
- use match statement when you **test a variable against many conditions** 
- match statement is an alternative of the if statement 

```python
# MATCH STATEMENT 
http_status = 500

match http_status:
    case 200 | 201:
        print("Success")
    case 400 :
        print("Bad Request")
    case 500 | 501:
        print("Server Error")
    case _:
        print("Unknown.")
```
```python
# Light switch example
# Light is currently off
current = False

if current:
    current = False
    print("Turning light off.")
else:
    current = True
    print("Turning light on.")
```
```python
# another example
loyalty_customer = True
total_bill = 120

if loyalty_customer and total_bill > 100:
    total_bill = total_bill - (float(total_bill) / 100) * 20
elif total_bill > 100:
    total_bill = total_bill - (float(total_bill) / 100)* 10
else:
    print("Sorry, no discount!")
print(f"Total bill is {float(total_bill)}")
```