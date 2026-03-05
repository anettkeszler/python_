
# from till 10, starting from 0 to 9, 10 is excluded - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range(10) 

#from 5 to 10, 10 is excluded - [5, 6, 7, 8, 9]
range(5, 10) 

# from 5 till 10, 10 is excluded, step is 2 - [5, 7, 9]
range(5, 10, 2) 

# from 10 till 1, 1 is excluded, backwards (step -1) - [10, 9, 8, 7, 6, 5, 4, 3, 2]
range(10, 1, -1)

my_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}

for k in my_dict:
    print(k, ":", my_dict[k])

print(2 in my_dict)

print(my_dict.keys()) 
print(my_dict.values())
print(my_dict.items())

print(list(my_dict.keys()))
print(list(my_dict.values()))
print(list(my_dict.items()))
print(my_dict.get(1)) # Coffee  
print(my_dict.get(4)) # None

print(my_dict.get(4, "alt if 4 not exists"))

print("Hello", "World!", sep="***")
print("Hello", "World", end="***")

