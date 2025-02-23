"""
Python List Methods with Examples
"""

# 1. append() - Adds an element to the end of the list
lst = [1, 2, 3]
lst.append(4)
print("append():", lst)  # [1, 2, 3, 4]

# 2. extend() - Adds multiple elements from an iterable
lst.extend([5, 6, 7])
print("extend():", lst)  # [1, 2, 3, 4, 5, 6, 7]

# 3. insert() - Inserts an element at a specific index
lst.insert(2, 99)
print("insert():", lst)  # [1, 2, 99, 3, 4, 5, 6, 7]

# 4. remove() - Removes the first occurrence of a value
lst.remove(99)
print("remove():", lst)  # [1, 2, 3, 4, 5, 6, 7]

# 5. pop() - Removes and returns an element at the given index (default: last)
popped = lst.pop()
print("pop():", lst, "| Removed Element:", popped)  # [1, 2, 3, 4, 5, 6] | Removed Element: 7

# 6. clear() - Removes all elements from the list
lst.clear()
print("clear():", lst)  # []

# Reset list for further examples
lst = [10, 20, 30, 40, 50, 20]

# 7. index() - Returns the index of the first occurrence of a value
index = lst.index(20)
print("index():", index)  # 1

# 8. count() - Returns the number of occurrences of a value
count = lst.count(20)
print("count():", count)  # 2

# 9. sort() - Sorts the list in ascending order
lst.sort()
print("sort():", lst)  # [10, 20, 20, 30, 40, 50]

# 10. sorted() - Returns a new sorted list without modifying the original
unsorted_list = [3, 1, 4, 1, 5, 9]
sorted_list = sorted(unsorted_list)
print("sorted():", sorted_list, "| Original List:", unsorted_list)  # [1, 1, 3, 4, 5, 9]

# 11. reverse() - Reverses the list in place
lst.reverse()
print("reverse():", lst)  # [50, 40, 30, 20, 20, 10]

# 12. copy() - Returns a shallow copy of the list
copy_lst = lst.copy()
print("copy():", copy_lst)  # [50, 40, 30, 20, 20, 10]

# 13. del statement - Deletes elements from the list using index
del lst[2]
print("del statement:", lst)  # [50, 40, 20, 20, 10]

# 14. List slicing - Removes last element using slicing
lst = lst[:-1]
print("List slicing (remove last element):", lst)  # [50, 40, 20, 20]
