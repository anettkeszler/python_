# ALGORITHM ANALYSIS, BIG O NOTATION 

## What is Algoritm?
- Algorithm is a generic, step-by-step list of instructions for solving a problem (given an input, the algorithm produces the desired output/result)
- refactoring an algoritm is a standard part of the software development cyclem, to making it faster or to perform better

### Algorithm Analysis
- an algorithm can be measured by **space**(how much memory it uses) and **time** (**execution time or running time**, how long it takes to run the code).<br>
- **Big O notation** is a fundamental concept in computer science and programming that helps you analyze and describe the efficiency of algorithms. It provides a standardized way of expressing how the runtime or resource usage of an algorithm grows as the size of the input data increases.
- **Benchmark analysis**: we track the actual time required for the program to compute its result.
In the time module there is a function called **time** that will return the current system clock time in seconds since some arbitrary starting point. By calling this function twice, at the beginning and at the end, and then computing the difference, we can get an exact number of seconds (fractions in most cases) for execution. 

```python
import time

def sum_of_n_(n):
    start = time.time()

    the_sum = 0
    for i in range(1, n + 1):
        the_sum += i

    end = time.time()
    return the_sum, end - start
```

## Big O Notation
- In terms of execution time, it is important to quantify the number of operations or steps that the algorithm will require. 
- When solving algorithms, we need to characterize their performance in terms of **best-case**, **worst-case**, or **average-case performance**. 
- Common functions for Big O:
![alt text](/screenshots/bigo_functions.png)

![alt text](/screenshots/bigo_functions2.png)


- **Constant time - O(1)** :  
    - same time and space regardless of the size
    - the runtime does not depend on the size of the input data
    - it remains constant, making it the **most efficient scenario**.
    - Example:
        1. **dictionary**: to get the value of an item you need by the key
        - the key is a direct pointer to the value and does not require any iteration to find 
        2. **accessing an element** in an **array by its index**
- **Logaritmic time - O(log n)**: 
    - the runtime grow logarithmically with the size of the input data (very efficient)
    - **binary search**: it splitting the list into 2 parts, and each time to check if a target is less than or greater than one. 
- **Linear time - O(n)**: 
    - this will grow depending on the size of the input 
    - array of integers with a range of 100, it will very fast. But if it increased to 1 million, it take a lot longer to complete 
    - Example: 
            - Searching for a specific value in an unsorted list (min, max, etc)
- **Log linear / Linearithmic time**(**O(n log n)**):
    - **Merge Sort algorithm**, which divides an array into smaller parts, sorts them, and then merges them back together.
- **Quadratic time - O (n2)**: 
    - the runtime grow with the square of the input size
    - Like checking every combination of items on a list against each other
    - Example: 
        - **nested list**
        - **Bubble Sort**
- **Exponencial time - O(2^n)**:
    - this occurs in algorithms where for each increase in the size of the data set, the runtime is doubled. 
    - **Fibonacci** 
- **Factorial runtime - O(n!)**:
    - terrible runtime 
    - Any algorithm that performs permutation on a given data set is an example of O(n!)

### Examples: 
- On many occasions you will need to make decisions between time and space trade-offs. 
#### Example 1: O(n^2) - nested loop
```python
test = 0
for i in range(n):
   for j in range(n):
      test = test + i * j
```
#### Example 2: O(n) -  Even though there are two loops they are not nested. You might think of this as O(2n) but we can ignore the constant 2.
```python
test = 0
for i in range(n):
   test = test + 1

for j in range(n):
   test = test - 1
```
#### Example 4: O(log n) - The value of i is cut in half each time through the loop so it will only take log n iterations.
```python
i = n
while i > 0:
   k = 2 + 2
   i = i // 2
```

### Performance of Lists
- the most common operations on lists are **indexing** and **assigning to an index position**. Both operations'performances are **O(1)**, no matter how large the list becomes.  
- another very common programming task is to grow a list:
    - **append() method - O(1)**
    - **concatenation - O(k) - k is the size of the list of concatenate**
    - **pop(0) - O(n)** -removing the first element
    - **pop() - O(1)** - removing the last element 
- creating list in different ways:
```python
def create_list():
    l = []
    for i in range(1000):
        l = l + [i]

def create_list2():
    l = []
    for i in range(1000):
        l.append(i)

def create_list3():
    l = [i for i in range(1000)]


def create_list4():
    l = list(range(1000))
```
- Big O Efficiency of Python List Operators:
![alt text](/screenshots/biogo_lists.png)

### Performance of Dictionaries
- you can access items by a key rather than a position (vs. lists)
- ```get item``` and ```set item``` operations are O(1).
- contains operation: O(1) (checking wether a key is in a dictionary or not) 

![alt text](/screenshots/bigo_dictionaries.png)

### Exercises with explanations:

**1.) Example**: 
- the outer loop runs **n times**
- for each iteration of the outer loop, the inner loop also runs **n times**
- the statement ```k = 2 + 2``` is a **constant time operation --> O(1)**
- total: **O(n²) (quadratic time)**
```
for i in range(n):
   for j in range(n):
      k = 2 + 2
```
**2.) Example**:
    - total: **O(n×1)=O(n)** 
```
for i in range(n):
     k = 2 + 2
```
**3.) Example**:
- Each iteration divides i by 2 --> So the number of iterations is the number of times you can divide n by 2 until it reaches 0.
- k = 2 + 2 is O(1) (constant time)
- total: **O(logn)×O(1)=O(logn)**
- Every step cuts the problem in half, which is the hallmark of logarithmic algorithms (similar to binary search).
```
i = n
while i > 0:
    k = 2 + 2
    i = i // 2
```
**4.) Example**:
- Each loop runs **n times** and performs a **constant-time operation k = 2 + 2**.
- First loop → O(n)
- Second loop → O(n)
- Third loop → O(n)
- Since the **loops are sequential** (not nested), we add their costs:
- total: **O(n)+O(n)+O(n)=O(3n) **
- Big-O ignores constant factors: **O(n)**
```
for i in range(n):
   k = 2 + 2
for j in range(n):
   k = 2 + 2
for k in range(n):
   k = 2 + 2
```
5.) **Example: Devise an experiment to verify that the list index operator is O(1)**.
- Expected Result: 
        - The time should stay roughly constant even as n increases.
        - This shows the operation does not depend on the list size.
```
import time

sizes = [1000, 10000, 100000, 1000000]
repetitions = 1000000

for n in sizes:
    lst = list(range(n))

    start = time.time()
    
    for _ in range(repetitions):
        x = lst[n//2]   # index access
    
    end = time.time()

    print(f"n={n}, time={end-start}")
```

### Cracking The Coding Interview - Big O Examples
1.) O(n) 


