l1 = [1,2,3,4,5]
l2 = [3,4,5,6,7]

l3 = l1+l2
l4 =[]
for i in l3:
    if i not in l4:
        l4.append(i)

print(l4)