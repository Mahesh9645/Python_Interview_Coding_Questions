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

##################################################################################################################################
#2.sum of even numbers of list
list2 = [1,2,3,4,5,6,7,8,9,10]
even_numbers =[]
odd_numbers=[]
for list in list2:
    if list %2==0:
        even_numbers.append(list)
    else:         #else if list % =! 0:
        odd_numbers.append(list)

# even_numbers1 = sum([i for i in list2 if i%2==0 ])
# odd_numbers1 = sum([i for i in list2 if i%2!=0 ])
# print(even_numbers1,odd_numbers1)


print(f'even numbers are :,{even_numbers} \nodd numbers are : {odd_numbers}')

##################################################################################################################################

#3.find largest  number and minimum number
list3 = [10,546,94,99,24,73,11,77,63,95]
max_number = list3[0]
min_number =list3[0]
# print(f'minimum number :,{min(list3)},\nmax number :, {max(list3)}')
for list in list3:
    if list > max_number:
        max_number = list
    elif list < min_number:
        min_number = list
print(f'max number is : {max_number},\nminimum number is :{min_number}')

# sorted_list = list3.sort(reverse=True)
# sorted_list =sorted(list3,reverse=True)
# print(sorted_list[1])

# second max number
# largest = max(list3)
# second_largest = max([i for i in list3 if i!=largest])
# print(second_largest)
##################################################################################################################################

#4 sum of given list
list4 = [10,20,30, 40, 50, 60]
sum_list = 0
for list in list4:
    sum_list += list
print(f'sum list is : {sum_list}')

##################################################################################################################################

#5.remove all duplicates in alist

list5 = [1,2,3,4,5,64,3,2,1,1,2,3,4,1,2,3,4,5,1,2,3,4,5,9,4,3,6,4,2]
new_list = []
for i in list5:
    if i not in new_list:
        new_list.append(i)
print(new_list)

# uniq_list = []
# op = [uniq_list.append(i) or i for i in list5 if i not in uniq_list]
# print(op)
##################################################################################################################################
list6 = [1,[2,3],4,5,[6,7],8,'Python',['test1','test2']] 

flattened_list = []
for item in list6:
    if isinstance(item, list):
        flattened_list.extend(item)
    else:
        flattened_list.append(item)

print(flattened_list)

 









    

