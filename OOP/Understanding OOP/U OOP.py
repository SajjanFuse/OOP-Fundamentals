"""
Sajjan Acharya
10:19, 12th April, 2024
Understanding Basic OOP concepts in Python 
"""

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house.lower() not in ["Gryffindor".lower(), "Hufflepuff".lower(), "Ravenclaw".lower(), "Slytherin".lower()]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return self.name

st = Student(input("Enter a name"), input("Enter your Hogwarts House"))

print(st)

# Some important notes
"""
Decorators: 
    - functions to define properties? 
    - @....
    - to harden the code 

    in __init__, it has self.name
    But in setter and getter, 
    Use _name as attributes
    and the setter and getter will have same name as function
    but have _name as the attribute inside them 

     
    - Getter and Setter 
        - @property
        - name(self):
            return self._name
        - @name.setter
        - name(self, name):
            self._name = name 

    - Class Methods 
    @classmethod
            
"""

