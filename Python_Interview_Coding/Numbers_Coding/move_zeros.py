#1.move all zeros to one end
list1 = [1,0,2,0,2,3,0]
zeros =[]
non_zeros =[]
for i in list1:
    if i==0:
        zeros.append(i)
    else:
        non_zeros.append(i)
print(non_zeros+zeros)

# non_zeros = [i for i in list1 if i !=0]
# zeros =list1.count(0)
# print(non_zeros + zeros*[0])