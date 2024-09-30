# string
a ="mahesh"
c ="mahesh"
print(a[::-1])
# method 2
b=""
count =0
for i in range(len(a)-1,-1,-1):
    b +=a[i]
for i in c:
    count = count +1
print(b)
print(count,"hgygyg")
###################################################################
# reverse a list
a = [1,2,3,4,5,6]
print(a[::-1])
# method 2
b=[]
for i in range(len(a)-1,-1,-1):
    b.append(a[i])
print(b)

# method 3
print(list(reversed(a)))

