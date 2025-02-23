# Parent class 1
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a generic sound.")

# Parent class 2
class Swimmer:
    def swim(self):
        print(f"{self.name} is swimming.")

# Child class inheriting from both Animal and Swimmer
class Duck(Animal, Swimmer):
    def __init__(self, name):
        # Initialize the 'name' attribute using Animal's constructor
        Animal.__init__(self, name)

    def speak(self):
        print(f"{self.name} quacks.")

# Creating an object of the Duck class, which inherits from both Animal and Swimmer
donald = Duck("Donald")

# Accessing methods from both parent classes
donald.speak()  # Output: Donald quacks. (from Animal, overridden in Duck)
donald.swim()   # Output: Donald is swimming. (from Swimmer)

"""
Python uses the Method Resolution Order (MRO) to determine the order 
in which classes are searched for methods or attributes
"""