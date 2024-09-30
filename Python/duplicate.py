list = [9,11,12,13,1,2,3,4,1,1,2,3,4,5,14,5,6,7,8,10,10,15,15]

for i in range(len(list)):
    for j in range(len(list)-1):
        if list[j] > list[j+1]:
            list[j] , list[j+1] = list[j+1],list[j]
print(list)
print(list[-1])
print(list[0])
print(round(sum(list)/len(list)))

# list = set(list)

# print(list)
print(list)
non_duplicate_list = []
for i in list:
    if i not in non_duplicate_list:
        non_duplicate_list.append(i)

print(non_duplicate_list)