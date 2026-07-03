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

A static method does not depend on either object data or class data.

It behaves like a normal function placed inside a class.

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

Encapsulation is the process of wrapping data and methods together into a single unit (class).

It also controls direct access to data.

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
