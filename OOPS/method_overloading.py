"""
Method Overloading Using Three Methods
---------------------------------------
Demonstrates the use of three distinct methods to simulate overloading.
"""

class Calculator:
    def add_two_numbers(self, a, b):
        """
        Adds two numbers.
        """
        return a + b

    def add_three_numbers(self, a, b, c):
        """
        Adds three numbers.
        """
        return a + b + c

    def add_four_numbers(self, a, b, c, d):
        """
        Adds four numbers.
        """
        return a + b + c + d


# Creating an object of the Calculator class
calc = Calculator()

# Calling the three methods with different numbers of arguments
result1 = calc.add_two_numbers(5, 10)       # Adds 5 + 10
result2 = calc.add_three_numbers(5, 10, 15) # Adds 5 + 10 + 15
result3 = calc.add_four_numbers(5, 10, 15, 20) # Adds 5 + 10 + 15 + 20

# Printing the results
print("Result of adding two numbers:", result1)         # Output: 15
print("Result of adding three numbers:", result2)       # Output: 30
print("Result of adding four numbers:", result3)        # Output: 50
