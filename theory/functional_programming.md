# FUNCTIONAL PROGRAMING

### List comprehension

```python
sq_list = []
for x in range(1, 11):
    sq_list.append(x * x)

print(sq_list)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# above example with list comprehension n one line
sq_list=[x * x for x in range(1, 11)]  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# using list comprehension with condition 
sq_list=[x * x for x in range(1,11) if x % 2 != 0]
print(sq_list) # [1, 9, 25, 49, 81]
```