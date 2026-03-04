# Python language

### What is programming? 
- **Programming** is a set of instructions in a programming language that the computer understands and performs a specific task. 
- To manage the complexity of problems and the problem-solving process, computer scientists use **abstractions** to allow them to focus on the “big picture” without getting lost in the details.
- By creating models of the problem domain, we are able to utilize a better and more efficient problem-solving process. These models allow us to describe the data that our algorithms will manipulate in a much more consistent way with respect to the problem itself.
- **Data abstraction**: For example, we do not necessarily know how the square root(math.sqrt()) is being calculated, but we know what function is called and how to use it. If we perform the import correctly, we can assume that the function will provide us with the correct results. We know that someone implemented a solution to the square root problem, but we only need to know how to use it.<br>
By providing this level of abstraction, we are creating an **encapsulation** around the data. The idea is that by encapsulating the details of the implementation, we are hiding them from the user’s view. This is called **information hiding**.
- **How abstract data types work**: The user interacts with the interface, using the operations that have been specified by the abstract data type. The abstract data type is the shell that the user interacts with. The implementation is hidden one level deeper. The user is not concerned with the details of the implementation.

### Python
- was released in 1991 by Guido van Rossum
- one of the most popular programming languages to learn 
- has lots of frameworks and libraries, packages and modules
- widely used in all areas of business (web developement, AI, machine learning, data analytics, applications)
- easy to learn and get started with
- require less code in comparison to Java, so it makes developers very productive and allows projects to be completed more quickly 
- "write less, do more" philosophy
- object-oriented language, but can be procedural and functional (paradigms)
- **interpreted language**: when we run the script, it is **first compiled and then interpreted/executed line by line**. The compilation part is mostly hidden from the user. While running the code, Python generates a byte code internally (Python interpreter - pyton code into byte code), this byte code is then converted using a python virtual machine(VM) to generate the output.  
- we define **classes** as a description of the data (which has attributes and behavior). 
- data items are called **objects**, which is an **instance of a class**. 

### Comments in Python code
- Reasons of commenting: 
    - Explaining what the code is intended to do    
    - Let developers know that code is deprecated
    - Add TODO comments for work to be completed at a later time
- Single-line comments: ```# I'm a single line comment```
- Multi-line comments: triple single quotes or triple double quotes (``` OR """) - used for docstrings or long comments
- Inline comments: ```x = 2  # resetting size```

### Installing Python path (Mac)
- **Xcode**: command-line tool, an integrated development environment (IDE), and you need to be installed to use brew
- **homebrew**: free, open-source **package manager** for macOS and Linux that simplifies installing, updating, and managing software via the command line
```
python --version
brew install python 
python3 --version
```
- homebrew will install python 3.x. version
- after installation, you need to set the paths to point to the brew install of python3
- First, let's figure out where it was installed by the package manager brew. Run the following command: 
```
brew info python
```
- ```/opt/homebrew/opt/python@3.x/libexec/bin``` is the one you want to use and set for your path.

1. Open zsh or bash (depending which shell you are using)
- Zsh: ```vim ~/.zshrc```
- Bash: ```vim ~/.bashrc```

2. Add the following line and remember to replace 3.x with the Python version that was installed on your system: 
```export PATH="/opt/homebrew/opt/python@3.x/libexec/bin:$PATH" ```
3. esc + wq!
4. Run the following:
- For Zsh shell: ```source ~/.zshrc``` 
- For Bash shell: ```source ~/.bashrc``` 

### Running Python code - Python Shell or VSCode
- in VSCode set up the python interpreter: search for 'python: select interpreter' (cmd+shift+p), choose the one it's recommended or which comes with the most recent version 
- **Python interpreter** is the program that reads and executes Python code. It converts Python code into machine code (byte code) that computer can execute. 

Different ways to run Python code:
1. **Interactive Shell in Terminal**:<br>
- to start: ```python```
- to exit: ```exit()```
- useful for running and testing small scripts
- no need to create a .py file

2. **Run a Python file**: <br>
```python3 hello.py```
- It is better to run Python in VSC, because VS Code features include auto-completion, code syntax, highlighting and debugging, whitespace and indentation helpers. 

3. **Run a Python file in Interactive mode**:<br>
```python3 -i hello.py```
