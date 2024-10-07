
"""
In hierarchical inheritance, multiple child classes inherit from the same parent class. 
Each child class can extend or modify the functionality of the parent class independently.
"""

class Animal:
    def speak(self):
        print("Animal makes a sound.")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        print("Dog barks.")

class Cat(Animal):  # Cat also inherits from Animal
    def speak(self):
        print("Cat meows.")

# Creating objects of Dog and Cat
dog = Dog()
cat = Cat()

dog.speak()  # Output: Dog barks.
cat.speak()  # Output: Cat meows.
