"""
Create a Python class to represent a University. 
The university should have attributes like name, location, and a list of departments. 
Implement encapsulation to protect the internal data of the University class. 
Create a Department class that inherits from the University class. The Department class should have attributes like department name, head of the department, and a list of courses offered. 
Implement polymorphism by defining a common method for both the University and Department classes to display their details. 
"""
import logging

class University:
    def __init__(self, name, location):
        # single underscore for the protected members 
        # double underscores for private members
        self.__name = name
        self._location = location
        self._departments = []

    @property
    def name(self):
        return self.__name

    @property
    def location(self):
        return self._location

    @property
    def departments(self):
        return self._departments

    def add_department(self, department):
        if isinstance(department, Department):
            self._departments.append(department)
        else:
            logging.error("Can only add Department objects to University")

    # common method for depart to display
    def display_details(self):
        print(f"University Name: {self.__name}")
        print(f"Location: {self.location}")
        print("Departments:")
        for department in self.departments:
            print(f"\t- {department.name}")

# Department inherited from University
class Department(University):
    def __init__(self, name, head_of_department, courses_offered):
        super().__init__("Department", "Location")  # Dummy values for superclass initialization
        self._name = name
        self._head_of_department = head_of_department
        self._courses_offered = courses_offered

    @property
    def name(self):
        return self._name

    @property
    def head_of_department(self):
        return self._head_of_department

    @property
    def courses_offered(self):
        return self._courses_offered

    # common method for depart
    def display_details(self):
        print(f"Department Name: {self.name}")
        print(f"Head of Department: {self.head_of_department}")
        print("Courses Offered:")
        for course in self.courses_offered:
            print(f"\t- {course}")


try:
    university = University("Example University", "Example Location")
    
    department1 = Department("Computer Science", "Ram Shrestha", ["Python", "JavaScript", "C++"])
    department2 = Department("Mathematics", "Hari Poudel", ["Calculus", "Algebra", "Commerce"])

    # Add departments to the university
    university.add_department(department1)
    university.add_department(department2)

    # Display university details
    university.display_details()

    print("\nDisplaying details of each department:")
    for department in university.departments:
        department.display_details()

except Exception as e:
    logging.exception("An error occurred:")

