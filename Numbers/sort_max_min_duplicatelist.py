# ascending order give list
list = [1,4,8,3,6,7,2,5,9]

# print(sorted(list))
# print(sorted(list,reverse=True))

# with bubble sort
for i in range(len(list)):
    for j in range(len(list)-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]

print(list)


data = [1, 3, 9, 5, 6, 7, 0, 2]
 
# Repeat the process until the list is sorted
swapped = True
while swapped:
    swapped = False  # Assume no swaps will be needed
    for i in range(len(data) - 1):
        if data[i] > data[i+1]:
            # Swap if the current element is greater than the next
            data[i], data[i+1] = data[i+1], data[i]
            swapped = True  # A swap was made, so we need another pass
 
print("Sorted list:", data)


# merge 2 arrays
a =[1,2,3]
b =[3,4,5]
print(a+b)

# max no for list
print(max(list), min(list))

# max no in a list
list = [22,34,65,87,91,65,33,44,91,34,44]

max = list[0]
for i in range(len(list)):
    if max < list[i]:
        max = list[i]

print(max)

# remove duplicate
uniqu_list = []

for i in range(len(list)):
    if list[i] not in uniqu_list:
        uniqu_list.append(list[i])

print(uniqu_list)