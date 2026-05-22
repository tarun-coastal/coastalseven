# Parent Class
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


# Child Class
class Employee(Person):

    def __init__(self, name, age, salary):

        # Call Parent Constructor
        super().__init__(name, age)

        # Child Property
        self.salary = salary

    def display_employee(self):

        # Call Parent Method
        super().display()

        print(f"Salary : {self.salary}")


# Object Creation
e1 = Employee("Rahul", 25, 50000)

# Method Call
e1.display_employee()