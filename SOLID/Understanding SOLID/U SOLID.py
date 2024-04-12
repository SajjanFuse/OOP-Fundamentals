"""
Sajjan Acharya
12:40, 12th April, 2024
Understanding basics of SOLID Principles and trying new examples
"""

# Basic Notes about SOLID
"""
SOLID: 
    - 5 object oriented design principles 
        - Single-responsibility principle (SRP)
        - Open-closed principle (OCP)
        - Liskov substitution principle (LSP)
        - Interface segregation principle (ISP)
        - Dependency inversion principle (DIP)
    - Single Responsibility Principle
        - A class should have only one reason to change.
        - class should have only one responsiblity 
        - not directly tied to the number of methods
            - but to core task a class is responsible for 
        - if a class has more than one job, the class becomes coupled 


    - Open-Closed Principle 
        - software entities to be open for extension, not modification
            - entities like classes, modules, functions 
        - 
    
    - Liskov Substitution Principle (LSP)
        - subtypes must be substitutable for their base types
        - making subclasses behave like their base class 
            - no breaking when calling the same methods 
            - 
        - __setattr__() of Python's attribute-setting mecanism 
        - If the code finds itself checking the type of class then, it must have violated this principle.
        - objects should be replaceable by their subtypes without altering how the program works

    - Interface Segregation Principle (ISP)
        - Clients should not be forced to depend upon methods that they do not use. 
            - Interfaces belong to clients, not to hierarchies
        - if a class doesn’t use particular methods or attributes, 
           then those methods and attributes should be segregated into more specific classes.
        - 


"""


# example of ISP, copied from https://gist.github.com/dmmeteo/f630fa04c7a79d3c132b9e9e5d037bfd?authuser=0#file-2-ocp-py-L93
class IShape:
    def draw_square(self):
        raise NotImplementedError
    
    def draw_rectangle(self):
        raise NotImplementedError
    
    def draw_circle(self):
        raise NotImplementedError

"""
This interface draws squares, circles, rectangles. class Circle, Square or Rectangle implementing the IShape 
interface must define the methods draw_square(), draw_rectangle(), draw_circle().
"""

class Circle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass
    
    def draw_circle(self):
        pass

class Square(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass
    
    def draw_circle(self):
        pass

class Rectangle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass
    
    def draw_circle(self):
        pass

"""
It's quite funny looking at the code above. class Rectangle implements methods (draw_circle and draw_square) it has no use of, 
likewise Square implementing draw_circle, and draw_rectangle, and class Circle (draw_square, draw_rectangle).
If we add another method to the IShape interface, like draw_triangle(),
"""

class IShape:
    def draw_square(self):
        raise NotImplementedError
    
    def draw_rectangle(self):
        raise NotImplementedError
    
    def draw_circle(self):
        raise NotImplementedError
    
    def draw_triangle(self):
        raise NotImplementedError


"""
the classes must implement the new method or error will be thrown.
"""


"""
Dependency Inversion Principle (DIP):
    - Abstractions should not depend upon details. Details should depend upon abstractions
    - tightly coupled classes can lead to scalibility issues 
    - classes dependent on abstractions rather than on concrete implementations 
        A. High-level modules should not depend upon low-level modules. Both should depend upon abstractions.
        B. Abstractions should not depend on details. Details should depend upon abstractions
"""