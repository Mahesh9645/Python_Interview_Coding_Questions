# reverse_vs_reversed.py

# Using reverse()
print("Using reverse():")
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# reverse() reverses the list in place
my_list.reverse()
print("List after reverse():", my_list)

# Using reversed()
print("\nUsing reversed():")
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# reversed() returns an iterator, so we convert it to a list
reversed_list = list(reversed(my_list))
print("Reversed list using reversed():", reversed_list)
print("Original list after reversed():", my_list)  # Original list is unchanged

# Additional Examples
print("\nReversing other iterables:")

# Reversing a tuple
my_tuple = (10, 20, 30)
reversed_tuple = tuple(reversed(my_tuple))
print("Reversed tuple:", reversed_tuple)  # Output: (30, 20, 10)

# Reversing a string
my_string = "hello"
reversed_string = "".join(reversed(my_string))
print("Reversed string:", reversed_string)  # Output: "olleh"




"""
Key Differences:
Feature	                  reverse()	       reversed()
Type	                  List method	   Built-in function
Modifies original	      Yes, in place	   No, returns a reversed iterator
Return value	          None            An iterator
Usage	Works only on lists	Works on any iterable
"""