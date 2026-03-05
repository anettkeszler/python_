# Data Types

## Built-in Atomic Data Types

### INTEGER, FLOAT - 'int' and 'float' - built-in numeric data types
- standard aritmetic operators: +, -, *, /,  ** (exponentiation)
- remainder/modulo(%) - returns the remainder of a division (123 % 10 = 3)
- integer division (//) - returns the integer portion of the quotient by truncating any fractional part (123 // 10 = 12)

### BOOLEAN - 'bool' 
- True or False 
- can be used with **logical operators**: and, or, not
- boolean data objects are also used as results for **comparison operators** (==, <, >, <=, >=, !=)

## Built-in Collection Data Types
- **ordered collections: List, string, tuples**
- **unordered collections: dictionary, set**

### LIST
- ordered built-in collections of any types of data objects
- In Python, it is a dynamic array that can hold any datatype 
- [] - empty list
- since lists are sequentially ordered, they support a number of operations that can be applied to any Python sequence:

![alt text](/screenshots/sequence_operations.png)

- List items can be accessed by its index
- List is iterable, you can iterate over it with a foor loop to access all items.
- List methods:
```python
nums.append(4)                  # add 4 at the end
nums.insert(0, 5)               # insert 5 at index 0
nums.extend(["z", 3, True])     # extend with iterable 
nums.remove(item)               # remove first occurance of item
nums.pop(i)                     # will remove the i-th item, and modify the original list 
nums.pop()                      # will remove the last item
nums.sort()                     # sort the list in-place
nums.reverse()                  # modify the list to be in reverse order with no return value
del nums[index]                 # removes the item on given index
nums.index(item)                # returns the index of the first occurance of item 
nums.count(item)                # returns the number of occurance of item
```
#### range() function
```python
# from till 10, starting from 0 to 9, 10 is excluded - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range(10) 

#from 5 to 10, 10 is excluded - [5, 6, 7, 8, 9]
range(5, 10) 

# from 5 till 10, 10 is excluded, step is 2 - [5, 7, 9]
range(5, 10, 2) 

# from 10 till 1, 1 is excluded, backwards (step -1) - [10, 9, 8, 7, 6, 5, 4, 3, 2]
range(10, 1, -1)
```

### STRING
- String is a sequence of characters enclosed in quotes (single or double) 
- if your string is too long for one line, you can add a backslash (```\```) at the end of each line to create a multi line declaration
- each character in the sequence can be accessed based on its index 
- length of the string: len() function
- concatenation: joining of separate strings with '+' operator 
- use ```'\n'``` to create a line break in a string
- to write a backslash in a normal string, write '```\\```'
- **String operations**: 
    - indexing
    - concatenation with the aritmetic operator (+)
    - multiply with * operator
    - slicing 
    - membership: in 
    - len()
- **String methods**: upper(), lower(), strip(), replace(), split(), join(), count(), center()
```python
print("a".upper())      # "A"
print("A".lower())      # "a"
print("  a ".strip())   # "a" --> remove spaces at the beginning and at the end of the string
print("abc".replace("bc", "ha"))    # "aha"
print("a b".split())    # ["a", "b"] --> splits a string into a list where each word is a list item
print("David".split("v")) # ["Da", "id"]
print("-".join(["a", "b", "c"]))    # "a-b-c" --> takes all items in an iterable and joins them into one string
print("abba".count("a")) # return the number of occurences of item in given string - 2 
print("abba".find("b")) # return the index of the first occurence of item - 1
```
- **String indexing and slicing**: 
```python
string[start:stop:step]
text = "Python"
text[0]         # "P"
text[-1]        # "n" --> last character
text[1:4]       # "yth" --> stop parameter is excluded
text[:3]        # "Pyt" --> from start, stop param excluded (0, 1, 2)
text[3:]        # "hon" --> to end
text[::2]       # "Pto" --> step parameter, every second 
text[::-1]      # "nohtyP" --> reverse

```
- **String formatting**: 
    - using f-string
    - format() method 
```python
name = "Jonathan"
age = 2

# f-string
print(f"Hello, {name}!")
print(f"{name} is {age} years old.")

# format() method
print("Hello, {}!".format(name))
print("{} is {} years old.".format(name, age))
```

#### STRING vs LIST:
- A major difference between lists and strings is that **lists can be modified while strings cannot**. 
- This is referred to as **mutability**. **Lists are mutable; strings are immutable.** For example, you can change an item in a list by using indexing and assignment. 


### TUPLE 
- my_tuple = ()
- tuples can accept any data types
- you can iterate over a tuple with a for loop
- key difference between lists and tuples, that tuples are **immutable**, means that they **can not be changed**
- **Immutability**: Once a tuple is created, its elements cannot be changed. 
- While you can access elements using indexing, you can't modify them or add new ones after creation

```python
# declare an empty tuple:
my_tuple = ()

# tuple can hold any data types
mixed_tuple = (1, "a", 3.14, True)

# access values is possible based on index
print(mixed_tuple[1])       # "a"
print(type(mixed_tuple))    # <class 'tuple'>

# tuple.count() - count the occurance of a value
print(mixed_tuple.count("b"))       # 0, 'b' is not in the tuple
print(mixed_tuple.count("a"))       # 1

# tuple.index() - get the index of given value
print(mixed_tuple.index(3.14))      # 2

# iterate over tuple
for x in mixed_tuple:
    print(x)
```

### SET
- Sets are collections with **no duplicates** and **unordered item** 
- Set is **not a sequence**, so it **cannot be indexed**. You cannot reach the items by its index (not ordered)
- Set methods:
    - **set.add(value)** - item will be added at the end
    - s**et.remove(value)** - given value will be removed
    - **set.discard(value)** - same as remove
- **Mathematical operations on sets**:
    - Union
    - Intersection
    - Difference
    - Symmetrical difference
    
```python
empty_set = {}

my_set = {1, 2, 3, 4, 5, 5}
print(my_set) # {1, 2, 3, 4, 5} no duplication

# add items to the set
my_set.add(6) # value will be added to the end

# remove() - remove item from the set
my_set.remove(2)    # number 2 will be removed

# discard() - does the same as remove
my_set.discard(3)   # number 3 will be removed
print(my_set)       # {1, 4, 5, 6}


# MATHEMATICAL OPERATIONS ON SET
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# union or | -  joins 2 sets without duplications
print(set1.union(set2))         # {1, 2, 3, 4, 5, 6, 7, 8}

# intersecion or & - give back values which occures in both sets
print(set1.intersection(set2))  # {4, 5}

# difference or '-' - get back all the elements that are only in set1, and not in set2
print(set1.difference(set2))    # {1, 2, 3}

# Symmetrical difference or ^ - get back all the elements that are present in set_a or set_b, but not in both sets
print(set1.symmetric_difference(set2))  # {1, 2, 3, 6, 7, 8}
```

### DICTIONARY
- Dictionaries access values based on keys (not on index as lists)
- Faster and more flexible as lists: you can go straight to the item you need based on its key
- we assign the key to a specific value --> called **key-value pair**
- Mutable, values can be changed or updated 
- If I try to add a duplicate key, it doesn't allow this, keys must be unique

```python
# access the value based on the key
my_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
print(my_dict[1]) # Coffee

# update the dictionary by replacing an item to another
my_dict[2] = 'Mint Tea' # update the value based on the key
print(my_dict)      # {1: 'Coffee', 2: 'Mint Tea', 3: 'Juice'}

# adding a key-value pair to the dictionary
my_dict[4] = 'Cocoa'
print(my_dict)       # {1: 'Coffee', 2: 'Mint Tea', 3: 'Juice', 4: 'Cocoa'}   

del my_dict[3]
print(my_dict)  # {1: 'Coffee', 2: 'Mint Tea', 4: 'Cocoa'} , delete the key-value pair based on the key

# Iterate over dictionaries
# this case only prints the keys:  1, 2, 3
for x in my_dict:
    print(x)        
    
for key, value in my_dict.items():
    print(str(key) + " : " + str(value))

# Output: 
# 1 : Coffee
# 2 : Mint Tea
# 4 : Cocoa

for k in my_dict:
    print(k, ":", my_dict[k])

print(2 in my_dict) # returns True if key is in the dictionary, False otherwise

print(my_dict.keys()) # returns the keys of the dictionary in a dict_keys object - dict_keys([1, 2, 3])
print(my_dict.values()) # returns the values of the dictionary in a dict_values object - dict_values(['Coffee', 'Tea', 'Juice'])
print(my_dict.items()) # Returns the key-value pairs in a dict_items object - dict_items([(1, 'Coffee'), (2, 'Tea'), (3, 'Juice')])

print(list(my_dict.keys())) # [1, 2, 3]
print(list(my_dict.values())) # ['Coffee', 'Tea', 'Juice']
print(list(my_dict.items())) # [(1, 'Coffee'), (2, 'Tea'), (3, 'Juice')]

print(my_dict.get(k)) # Returns the value associated with k, None otherwise
print(my_dict.get(1)) # Coffee  
print(my_dict.get(4)) # None
print(my_dict.get(4, "alt if 4 not exists"))  # alt if 4 not exists
```
