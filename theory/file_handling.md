# File handling

- File handling functions: **open()** and **close()** 
- Open():
    - ```open()``` function is used for reading, writing and creating files 
    - open() function accepts 2 arguments --> open(<file_name> OR <file_location>, <mode>)
        - mode indicates the action --> reading, writing, creating
            - 'r' --> open and read in text format
            - 'rb' --> open and read in binary format
            - 'r+' --> open, read and write 
            - 'w' --> open for writing 
            - 'a' --> open for editing or appending 
- ```close()``` function: no arguments, it closes the open connection 
- ```with open()``` function: it closes the file automatically, and better with exception handling
- reading files:
    - **read()** - provides the whole content of the file in a string
    - **readline()** - returns a single line as a string
    - **readlines()** - reads the whole content of the file and returns it as an ordered list allowing iteration on it

```python
# open and read from a file, than close the file
file = open('test.txt', 'r')
data = file.readline()  
print(data)
file.close()

# with open --> closes the file automatically
with open('test.txt', 'r') as file:
    data = file.readline() 
    print(data)

with open('new_file.txt', 'r') as file:
    data = file.read()
    print(data)
    print(type(data)) # string
```
```python
# creating a new file: file.write("")
with open('new_file.txt', 'w') as file:
    file.write('This is a new file created!') 
```
```python
# Editing a file with multiple lines: file.writelines("") --> accepts a list 
try: 
    with open('new_file.txt', 'a') as file:
        file.writelines(['\nThis is the first line!', '\nThis is the second line!', '\nThird line'])
except FileNotFoundError as e:
    print(e, "File not exists.")
```
