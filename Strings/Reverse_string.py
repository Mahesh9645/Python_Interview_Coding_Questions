name = "mahesh"
reverse_name = ""

# using slicing
# print(name[::-1])

# using loop
for i in name:
    reverse_name = i+reverse_name

print(reverse_name)

# checking palidrome
print(name == reverse_name)

# printingbforward direction
print("Forward direction")
for a in name:
    print(a, end='')

# printing backward direction
print("Backward direction")
for b in name[::-1]:
    print(b,end='')