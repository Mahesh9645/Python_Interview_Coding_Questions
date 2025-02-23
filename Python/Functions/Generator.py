"""
A generator is a special type of function in Python that allows you to 
produce a sequence of values lazily (one value at a time) using the yield statement.
"""

def generate_numbers(n):
    for i in range(n):
        yield i  # Yield returns one value at a time

# Using the generator
gen = generate_numbers(5)
for num in gen:
    print(num)  # Outputs: 0, 1, 2, 3, 4
