# printing numbers in list
l = list(range(1,10,1))
print(type(l),l)

# accessing with index
print(l[3]) #4

# accessing with slice
print(l[2:7:1])  #[3, 4, 5, 6, 7]

# display even numbers in list
print(l)
print(l[2])
for i in l:
    if i % 2 == 0:
        print(f"Index {i}: {i}")

print(f'length of the list : {len(l)}')

# count numbres
n=[1,2,2,2,2,3,3]
print(f'count no of times reoerated in list {n.count(2)}')

print(f'3 number position with index {n.index(3)}')

# insert function (index,value)-- it will append with particular position with number
# but it not delete its value
print(f'inserting new numer with undex,{n.insert(0,5),None}') #[5, 1, 2, 2, 2, 2, 3, 3

# extend --it add 2 list into one
l.extend(n)
print(l)

# remove--
print(f'remove from 9 from lis {l.remove(9)},\n{l}')


print(max(l))

c =[1,4,3,2]
print(c)