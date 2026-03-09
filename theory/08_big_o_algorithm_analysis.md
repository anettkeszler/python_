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





