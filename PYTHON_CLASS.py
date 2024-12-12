# Syntax:
#
# class ClassName:
#         <statement-1>
#         .
#         .
#         <statement-N>
#
# object_name = ClassName()

# --------------------------------------------------------------------------------------------#
class Car:
    def define(self, modelname, year):
        self.modelname = modelname
        self.year = year

    def display(self):
        print(self.modelname, self.year)


c1 = Car()
c1.define("Toyota", 2016)
c1.display()


# --------------------------------------------------------------------------------------------#
class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1
        print(self.name, self.age)


person1 = Person("Ayan", 25)
person2 = Person("Bobby", 30)
print(Person.count)


# --------------------------------------------------------------------------------------------#
class Employee:
    def __init__(self, name, id):
        self.id = id
        self.name = name

    def display(self):
        print(self.id)
        print(self.name)


emp1 = Employee("John", 101)
emp2 = Employee("David", 102)
emp1.display()
emp2.display()


# --------------------------------------------------------------------------------------------#
# default construtor
class Student:
    roll_num = 101
    name = "Joseph"

    def display(self):
        print(self.roll_num, self.name)


st = Student()
st.display()


# --------------------------------------------------------------------------------------------#
class Student:
    def __init__(self):
        print("The First Constructor")

    def __init__(self):
        print("The second contructor")


st = Student()


# --------------------------------------------------------------------------------------------#
# Python built-in class functions
class Student:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

        # creates the object of the class Student


s = Student("John", 101, 22)

# prints the attribute name of the object s
print(getattr(s, 'name'))

# reset the value of attribute age to 23
setattr(s, "age", 23)

# prints the modified value of age
print(getattr(s, 'age'))

# prints true if the student contains the attribute with name id

print(hasattr(s, 'id'))
# deletes the attribute age
delattr(s, 'age')

# this will give an error since the attribute age has been deleted
print(s.age)


# # --------------------------------------------------------------------------------------------#
# class Student:
#     def __init__(self, name, id, age):
#         self.name = name;
#         self.id = id;
#         self.age = age
#
#     def display_details(self):
#         print("Name:%s, ID:%d, age:%d" % (self.name, self.id))
#
#
# s = Student("John", 101, 22)
#
# print(s.__dict__)
# -----------------------------------------------------------------------------------------------
# -----------ABSTRACTION--------------#
# class Office:
#     def __init__(self, name, baseSalary):
#         self.name = name
#         self.baseSalary = baseSalary
#         self.bonus = 10000
#
#     def calculateFinalSalary(self):
#         self.finalsalary = self.baseSalary + self.bonus
#         print(self.finalsalary)
#
#     def getempdetails(self):
#         self.calculateFinalSalary()
#
#
# e1 = Office("Anjlai", 20000)
# e1.getempdetails()

# # -----------------------------------------------------------------------------------------------
# -----------Encapsulation--------------#
class Employee:
    def setempdetails(self, redId, name, number):
        self.regId = redId
        self.name = name
        self.number = number
    def getregid(self):
        return self.regId
    def getname(self):
        return self.name
    def getnumber(self):
        return self.number
e1 = Employee()
e1.setempdetails(101, "anjali", "1234567890")
print(e1.getregid())
print(e1.getname())
print(e1.getnumber())
# # -----------------------------------------------------------------------------------------------
# # -----------inhertiance--------------#

# Single Inheritance: In single inheritance, a class inherits from only one base class.
# This is the simplest form of inheritance.
class Parent:
    def studetails(self, id, name):
        self.id = id
        self.name = name


class Child(Parent):
    def details(self, gender):
        self.gender = gender

    def display(self):
        print(self.id, self.name, self.gender)


c1 = Child()
c1.studetails(120, "Anjali")
c1.details("female")
c1.display()


# # # Multiple Inheritance: In multiple inheritance, a class can inherit from more than one base class.
# # # This allows a derived class to inherit attributes and methods from multiple parent classes.
# class Parent1:
#     pass
#
# class Parent2:
#
#     pass
#
# class Child(Parent1, Parent2):
#     pass
#
# #
# # # Multilevel Inheritance: In multilevel inheritance, a class inherits from another derived class.
# # # This creates a chain of inheritance.
# class Grandparent:
#     pass
#
# class Parent(Grandparent):
#     pass
#
# class Child(Parent):
#     pass
# #
#
# # Hierarchical Inheritance: In hierarchical inheritance, multiple classes inherit from a single base class.
# class Animal:
#     pass
#
# class Dog(Animal):
#     pass
#
# class Cat:
#     pass
#
# #
# #
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return self.name

class Cat(Animal):
    def speak(self):
        return self.name

# Create instances of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak method on each instance
print(dog.speak())  # Output: "Buddy says Woof!"
print(cat.speak())  # Output: "Whiskers says Meow!"
# #

#
#
#
# class Parent:
#     def __init__(self, name):
#         self.name = name
#
# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)  # Call the constructor of the Parent class
#         self.age = age
#         print(self.name)
#         print(self.age)
#
# child = Child("Anjali", 24)


class Student:
    # Constructor - non parameterized
    def __init__(self):
        print("This is non parametrized constructor")

    def show(self, name):
        print("Hello", name)


student = Student()
student.show("John")



class Animal:
    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Dog):
    def make_sound(self):
        print("Meow")



# Creating instances of Dog and Cat
c1 = Cat()
c1.make_sound()


