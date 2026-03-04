# Data Types

### Built-in Atomic Data Types

#### 'int' and 'float' - built-in numeric data types
- standard aritmetic operators: +, -, *, /,  ** (exponentiation)
- remainder/modulo(%) - returns the remainder of a division (123 % 10 = 3)
- integer division (//) - returns the integer portion of the quotient by truncating any fractional part (123 // 10 = 12)

#### boolean - 'bool' 
- True or False 
- can be used with **logical operators**: and, or, not
- boolean data objects are also used as results for **comparison operators** (==, <, >, <=, >=, !=)

### Built-in Collection Data Types
- **ordered collections: List, string, tuples**
- **unordered collections: dictionary, set**

#### Lists
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
nums.pop(i)                     # will remove the i-th item
nums.pop()                      # will remove the last item
nums.sort()                     # sort the list in-place
nums.reverse()                  # modify the list to be in reverse order
del nums[index]                 # removes the item on given index
nums.index(item)                # returns the index of the first occurance of item 
nums.count(item)                # returns the number of occurance of item

```
