"""This program demonstrates three methods to reverse a list in Python."""

# Original list
a = [1, 2, 3, 4, 5, 6]

# Method 1: Using slicing
print("Reversed list using slicing:", a[::-1])

# Method 2: Using a for loop to append elements in reverse order
b = []
for i in range(len(a) - 1, -1, -1):
    b.append(a[i])
print("Reversed list using loop:", b)

# Method 3: Using the built-in reversed() function
print("Reversed list using reversed():", list(reversed(a)))
