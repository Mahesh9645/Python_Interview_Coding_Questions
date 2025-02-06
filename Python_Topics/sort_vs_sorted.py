# sort_vs_sorted_simple.py

# Using sort()
my_list = [3, 1, 4, 1, 5]
print("Original list (before sort()):", my_list)

# sort() modifies the original list & returns none
my_list.sort()
print("List after using sort():", my_list)

# Using sorted()
another_list = [3, 1, 4, 1, 5]
print("\nOriginal list (before sorted()):", another_list)

# sorted() creates a new sorted list
new_list = sorted(another_list)
print("New sorted list:", new_list)
print("Original list (unchanged):", another_list)


"""
1. sort():
Modifies the list in place: It doesn't return a new list but sorts the original list.
Available only for lists: It's a method of list objects.


2. sorted():
Returns a new sorted list: The original list or iterable remains unchanged.
Works with any iterable: Can be used with lists, tuples, dictionaries, sets, etc.
Can sort items without modifying the original data.

"""