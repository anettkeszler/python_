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
    - open and read from a file, than close the file:
![alt text](/screenshots/file_readline.png)
![alt text](/screenshots/file_read_with_open.png)
- creating a new file: **file.write("")**:
![alt text](/screenshots/file_write_with_open.png)
- editing a file with multiple lines: **file.writelines("")** --> accepts a list 
![alt text](/screenshots/file_writelines_with_open.png)