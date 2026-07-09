# Object-Oriented Programming (OOP) in Python

# Object-Oriented Programming (OOP)

## What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm that organizes a program around **objects** instead of functions and logic. An object represents a real-world entity that contains both **data (attributes)** and **behavior (methods)**.

OOP helps developers write programs that are:
- Easy to understand
- Easy to maintain
- Reusable
- Secure
- Scalable

Python is a multi-paradigm language that fully supports Object-Oriented Programming.

---

# Why Use OOP?

OOP provides several advantages over procedural programming.

- Promotes code reusability
- Reduces code duplication
- Makes programs modular
- Improves maintainability
- Provides better data security
- Simplifies debugging and testing
- Makes large applications easier to develop

---

# Features of OOP

The four main pillars of OOP are:

1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

Other important concepts include:

- Class
- Object
- Constructor
- Methods
- Instance Variables
- Class Variables
- self keyword
- super() function

---

# Class

## Definition

A **class** is a blueprint or template used to create objects. It defines the properties (attributes) and behaviors (methods) that the objects created from it will have.

A class itself does not occupy memory for actual data until an object is created.

### Characteristics

- Blueprint of an object
- Defines attributes and methods
- Can create multiple objects
- Improves code organization

### Syntax

```python
class ClassName:
    # attributes
    # methods
```

---

# Object

## Definition

An **object** is an instance of a class. It is the actual entity that occupies memory and can access the properties and methods defined in the class.

Every object has:

- Identity
- State
- Behavior

### Characteristics

- Created from a class
- Stores actual data
- Can call methods
- Each object has its own state

### Syntax

```python
object_name = ClassName()
```

---

# Difference Between Class and Object

| Class | Object |
|--------|---------|
| Blueprint | Instance of class |
| Logical entity | Physical entity |
| Does not occupy memory for data | Occupies memory |
| Used to create objects | Created from a class |
| Defines structure | Represents actual data |

---

# Constructor

## Definition

A constructor is a special method that is automatically executed whenever an object is created.

In Python, the constructor is named:

```python
__init__()
```

Its primary purpose is to initialize the object's data.

### Characteristics

- Automatically called
- Initializes object variables
- Executes only once during object creation
- Can accept parameters

### Syntax

```python
def __init__(self, parameters):
    # initialization
```

---

# self Keyword

## Definition

The **self** keyword refers to the current object of the class.

It allows an object to access its own variables and methods.

### Why self is Required

- Represents the current instance
- Accesses instance variables
- Calls instance methods
- Distinguishes object variables from local variables

### Syntax

```python
self.variable_name
self.method_name()
```

---

# Variables in Python OOP

## Instance Variable

### Definition

Instance variables belong to individual objects.

Every object has its own copy of instance variables.

### Characteristics

- Created inside constructor
- Different for every object
- Stored separately

### Syntax

```python
self.variable_name = value
```

---

## Class Variable

### Definition

A class variable belongs to the class itself instead of individual objects.

It is shared among all objects.

### Characteristics

- Same value for every object
- Defined inside class but outside methods
- Uses less memory

### Syntax

```python
class ClassName:
    variable_name = value
```

---

# Methods

## Definition

Methods are functions defined inside a class.

They describe the behavior of objects.

---

## Instance Method

### Definition

Instance methods work with object-specific data.

They require the **self** parameter.

### Syntax

```python
def method_name(self):
    pass
```

---

## Class Method

### Definition

A class method works with class variables instead of object variables.

It uses the **@classmethod** decorator.

The first parameter is **cls**.

### Syntax

```python
@classmethod
def method_name(cls):
    pass
```

---

## Static Method

### Definition

A static method does not depend on either object data or class data. It behaves like a normal function placed inside a class.

Uses the **@staticmethod** decorator.

### Syntax

```python
@staticmethod
def method_name():
    pass
```

---

# Encapsulation

## Definition

Encapsulation is the process of wrapping data and methods together into a single unit (class). It also controls direct access to data.

### Advantages

- Data hiding
- Better security
- Controlled access
- Easier maintenance

---

## Access Specifiers

Python provides three levels of access.

### Public

Accessible from anywhere.

Syntax

```python
variable
```

---

### Protected

Accessible within the class and subclasses.

Represented using a single underscore.

Syntax

```python
_variable
```

---

### Private

Accessible only within the class.

Represented using double underscores.

Syntax

```python
__variable
```

---

# Inheritance

## Definition

Inheritance allows one class to acquire the properties and methods of another class.

The existing class is called the **Parent (Base) Class**.

The new class is called the **Child (Derived) Class**.

### Advantages

- Code reuse
- Reduced duplication
- Easy maintenance
- Better organization

### General Syntax

```python
class ChildClass(ParentClass):
    pass
```

---

# Types of Inheritance

## 1. Single Inheritance

One child inherits from one parent.

---

## 2. Multiple Inheritance

One child inherits from multiple parents.

---

## 3. Multilevel Inheritance

A child inherits from another child class.

---

## 4. Hierarchical Inheritance

Multiple child classes inherit from one parent.

---

## 5. Hybrid Inheritance

Combination of two or more inheritance types.

---

# Polymorphism

## Definition

Polymorphism means **one interface, multiple implementations**.

The same method can perform different tasks depending on the object.

### Advantages

- Flexibility
- Easy extension
- Better maintainability
- Code reusability

---

## Types of Polymorphism

### Method Overriding

A child class provides its own implementation of a method already defined in the parent class.

### Syntax

```python
def method_name(self):
    pass
```

---

### Method Overloading

Method overloading means creating multiple methods with the same name but different parameters.

Python does not support true method overloading directly.

It can be achieved using:

- Default arguments
- Variable-length arguments (`*args`, `**kwargs`)

---

# Abstraction

## Definition

Abstraction means hiding implementation details and exposing only essential functionality to the user.

Python provides abstraction through the **abc (Abstract Base Class)** module.

### Advantages

- Hides complexity
- Improves security
- Reduces code duplication
- Simplifies large applications

### Syntax

```python
from abc import ABC, abstractmethod

class ClassName(ABC):

    @abstractmethod
    def method_name(self):
        pass
```

---

# super() Function

## Definition

The **super()** function is used to access the parent class methods and constructor from the child class.

### Advantages

- Reuses parent functionality
- Avoids duplicate code
- Simplifies inheritance

### Syntax

```python
super().method_name()
```

or

```python
super().__init__()
```

---

# isinstance()

## Definition

Checks whether an object belongs to a particular class.

### Returns

- True
- False

### Syntax

```python
isinstance(object, ClassName)
```

---

# issubclass()

## Definition

Checks whether one class is derived from another class.

### Returns

- True
- False

### Syntax

```python
issubclass(ChildClass, ParentClass)
```

---

# Magic Methods (Dunder Methods)

## Definition

Magic methods are special methods surrounded by double underscores.

They automatically perform predefined operations.

Examples include:

- `__init__()` → Constructor
- `__str__()` → String representation
- `__repr__()` → Official representation
- `__len__()` → Length
- `__add__()` → Addition
- `__eq__()` → Equality comparison

General Syntax

```python
def __method__(self):
    pass
```

---

# Advantages of OOP

- Code Reusability
- Easy Maintenance
- Better Security
- Modularity
- Flexibility
- Scalability
- Easy Testing
- Real-world Modeling
- Improved Productivity

---

# Disadvantages of OOP

- Requires more planning
- Higher memory usage
- Slightly slower execution
- More complex for small programs
- Learning curve for beginners

---

# Additional Important OOP Topics

---

# 1. Destructor

## Definition

A destructor is a special method that is automatically called when an object is about to be destroyed.

## Characteristics

- Automatically called before object destruction
- Used to release resources
- Performs cleanup tasks

## Syntax

```python
def __del__(self):
    pass
```

---

# 2. Composition

## Definition

Composition is a relationship where one class contains an object of another class.

It represents a **Has-A** relationship.

## Characteristics

- Strong relationship
- Dependent objects
- Promotes code reuse
- Improves modularity

## General Syntax

```python
class ClassB:
    def __init__(self):
        self.object = ClassA()
```

---

# 3. Aggregation

## Definition

Aggregation is a relationship where one class uses another class, but both can exist independently.

It also represents a **Has-A** relationship.

## Characteristics

- Weak relationship
- Independent objects
- Supports code reuse

## General Syntax

```python
class ClassB:
    def __init__(self, obj):
        self.obj = obj
```

---

# 4. Association

## Definition

Association is a relationship in which two independent classes communicate with each other.

## Characteristics

- Independent objects
- Temporary relationship

## General Syntax

```python
class ClassB:
    def method(self, obj):
        pass
```

---

# 5. Duck Typing

## Definition

Duck Typing is a feature of Python where the type of an object is less important than the methods it implements.

"If it behaves like a duck, it is treated like a duck."

## Characteristics

- Behavior-based programming
- No explicit inheritance required
- Supports polymorphism

---

# 6. Method Resolution Order (MRO)

## Definition

Method Resolution Order (MRO) determines the order in which Python searches parent classes for a method during multiple inheritance.

## Syntax

```python
ClassName.mro()

ClassName.__mro__
```

---

# 7. Property Decorator

## Definition

The `@property` decorator allows a method to be accessed like an attribute.

## Advantages

- Supports encapsulation
- Provides controlled access
- Makes code cleaner

## Syntax

```python
@property
def method_name(self):
    pass
```

---

# 8. Getter, Setter and Deleter

## Getter Syntax

```python
@property
def attribute(self):
    pass
```

## Setter Syntax

```python
@attribute.setter
def attribute(self, value):
    pass
```

## Deleter Syntax

```python
@attribute.deleter
def attribute(self):
    pass
```

---

# 9. IS-A and HAS-A Relationship

## IS-A Relationship

Established through **Inheritance**.

### Examples

- Car IS-A Vehicle
- Dog IS-A Animal

---

## HAS-A Relationship

Established through **Composition** or **Aggregation**.

### Examples

- Car HAS-A Engine
- School HAS-A Teacher

---

# Shallow Copy and Deep Copy

## Definition

When we copy an object in Python, there are two ways:

1.  Shallow Copy
2.  Deep Copy

``` python
import copy
```

## Shallow Copy

A shallow copy creates a new object but shares nested objects.

``` python
import copy
list1=[[10,20],[30,40]]
list2=copy.copy(list1)
list2[0][0]=100
print(list1)
print(list2)
```

Output:

    [[100,20],[30,40]]
    [[100,20],[30,40]]

## Deep Copy

A deep copy creates completely independent copies.

``` python
import copy
list1=[[10,20],[30,40]]
list2=copy.deepcopy(list1)
list2[0][0]=100
print(list1)
print(list2)
```

Output:

    [[10,20],[30,40]]
    [[100,20],[30,40]]

## Difference

  Shallow Copy               Deep Copy
  -------------------------- -----------------------
  Copies outer object only   Copies entire object
  Shares nested objects      Copies nested objects
  Faster                     Slower
  Less memory                More memory

---

# Data Hiding (Name Mangling)

## Definition

Data hiding restricts direct access to an object's data using private
variables (`__variable`).

## Public Variable

``` python
class Student:
    def __init__(self):
        self.name='Zaman'
```

## Protected Variable

``` python
class Student:
    def __init__(self):
        self._roll=101
```

## Private Variable

``` python
class Student:
    def __init__(self):
        self.__marks=95
    def show(self):
        print(self.__marks)
```

Direct access:

``` python
print(s.__marks)
```

Raises AttributeError.

