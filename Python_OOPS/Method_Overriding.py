"""
Method Overriding Example
--------------------------
A child class overrides a method of the parent class to provide specific behavior.
"""

class Animal:
    def speak(self):
        """
        Generic method to describe the sound an animal makes.
        """
        print("Animal makes a sound.")

class Dog(Animal):
    def speak(self):
        """
        Specific method to describe the sound a dog makes.
        """
        print("Dog barks.")

class Cat(Animal):
    def speak(self):
        """
        Specific method to describe the sound a cat makes.
        """
        print("Cat meows.")


# Create objects of each class
animal = Animal()  # Parent class object
dog = Dog()        # Child class (Dog) object
cat = Cat()        # Child class (Cat) object

# Call the speak method on each object
animal.speak()  # Output: Animal makes a sound.
dog.speak()     # Output: Dog barks.
cat.speak()     # Output: Cat meows.
