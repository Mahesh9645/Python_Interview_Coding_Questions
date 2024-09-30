n =10
f1 =[0,1]

for i in range(2,n):
    f =f1[-1] +f1[-2]
    f1.append(f)

print(f1)

# factorial

n=5
sum =1
for i in range(n):
    sum += sum *i

print(sum)