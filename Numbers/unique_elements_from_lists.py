# List 1
l1 = [1, 2, 3, 4, 5]

# List 2
l2 = [3, 4, 5, 6, 7]

# Combine both lists
l3 = l1 + l2

# Create a new list to hold unique elements
l4 = []
for i in l3:
    if i not in l4:  # Check if the element is not already in l4
        l4.append(i)  # Append the unique element to l4

# Print the list of unique elements
print("Unique elements from combined lists:", l4)
