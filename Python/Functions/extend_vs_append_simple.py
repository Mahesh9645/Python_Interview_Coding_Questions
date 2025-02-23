# extend_vs_append_simple.py
# ================
# append()--> will add single value
# extend ()--> will add  2 or more values
# Using append()
print("Using append():")
my_list = [1, 2, 3]
print("Before append:", my_list)

# Append a single element
my_list.append(4)
print("After appending 4:", my_list)

# Append a list (adds it as a single element)
my_list.append([5, 6])
print("After appending [5, 6]:", my_list)

print("\nUsing extend():")
# Using extend()
my_list = [1, 2, 3]
print("Before extend:", my_list)

# Extend with another list (adds each item separately)
my_list.extend([4, 5, 6])
print("After extending with [4, 5, 6]:", my_list)

# Extend with a string (adds each character separately)
my_list.extend("78")
print("After extending with '78':", my_list)

# Summary of the difference
print("\nSummary:")
print("- append() adds a single item to the list (even if it’s a list).")
print("- extend() adds each element of an iterable separately to the list.")
