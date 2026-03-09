### Object Oriented Programming
- relies on simplicity and reusability to improve workflow 
- is a way of structuring your code
- OOP translates real-world problem into code
- Class: logical code block containing attributes(variables) and behaviors(methods)
- A class provides a blueprint for creating an object
- an object is an instance of a class 
- instanciation: creating an instance of a class 
- OOP concepts:
    - **Inheritance**: creation of a new class by deriving from an existing class. Parent class or super class is the original, and any derivatives are the subclass or child class. 
    - **Polimorphism**: a single function can act differently depending on the object. Example: the built-in '+' operator works differently for different datatypes. (for strings: concatenation, for numbers: abstraction)
    - **Encapsulation**: Python can bind methods and variables from direct access by wrapping them within a single unit of scope, such as a class. Helps prevent unwanted modifications. It is used for hiding data and its internal representation. 
    - **Abstraction**: hide implementation details to make data safer 

#### Classes and Instances / + 17_oop.py
- Classes have attributes(variables) and behaviors(methods)
- everything in Python is an object or derived from the object class 
- Instantiation:
    - 1. Class definition
    - 2. Creayting a new instance 
    - 3. Initializing the new instance 
- Use functionalities of a class in 2 ways:
    - call the class directly or 
    - instantiating an object of the class 

#### Instance methods 
- You can change an instance's methods and variables without effecting other instances

#### Parent classes and Child classes (inheritance)
- Every class in Python inherits from a built-in base class called Objects 
```
class MyClass() --> inherited from class MyClass(object)
```
- **Parent/Super/Base Class** 
- The class which inherits from it is the **Child/Sub/Derived Class**
- The Child class extends the variables and methods of its parent class
    - you can add new properties to the child class 
    - you can modify inherited properties in the child class without affecting the parents
- If class A is the parent class and class B is inheriting from it, then class A is passed inside class B as a parameter. This will allow class B to directly access the attributes and methods inside class A.
```
class A:
    pass
class B(A):
    pass


#### Multiple inheritance
```
class A:
   a = 1
   
class B:
   b = 2
   
class C(A, B):
   pass

c = C()
print(c.a, c.b)
```
- issubclass() and isinstance() methods help to understand the relation between classes
```
issubclass(child, parent)
isinstance(c, B)
```
- super() function: can be called inside the derived class and gives access to the methods and variables of the parent classes or sibling classes.
- Sibling classes are the classes that share the same parent class. 
-  When you call the super() function, you get an object that represents the parent class in return.

#### Abstract classes and methods
- the methods we define in an abstract class are guaranteed to be present in the derived class , because they must be implemented 
- you cannot create an instance from an abstract class 
- python doesn't support abstraction directly, you need to impose a module just to define an abstract class 
- methods in an abstract class needs to be defined before they can be implemented 
- key advantage is to hide the details of implementation without sacrificing functionality
- Implementation of abstract classes can done in 2 ways: 
    - the methods must be implemented by the derived class 
    - super() function
```
from abc import ABC, abstractmethod 

class Employee(ABC):

    @abstractmethod
    def donate(self):
        pass

class Donation(Employee):
    def donate(self):
        a = input("How much would you like to donate?: ")

amounts = []

john = Donation()
j = john.donate()
amounts.append(j)

peter = Donation()
p = peter.donate()
amounts.append(p)
```
#### Method Resolution Order - MRO
- Simple inheritance: 
- Multiple inheritance: 1 child class inheriting from more than 1 parent 
- Multi level inheritance:  inheritance taking place on several levels 
- Hierarchical inheritance: several sub classes inherit from a common parent 
- Hybrid inheritance: mixes characterictics of the others 
- MRO: determines the order in which a given method or attribute passed in searched 

