n = 9474

pow = len(str(n))
sum = 0
for digits in str(n):
    sum += int(digits) ** pow

print(sum == n)

print(len(str(n)))


# print prime number between 10 to 50

a =10
b=50
for i in range(3,10):
    is_prime = True
    for j in range(2,i):
        if i%j == 0:
            is_prime =False
            print(i,"its not a prime")
            break
    if is_prime:
        print(i,"its a prime number")

# second lagest number----->swaPPING

list = [22,34,65,87,91,65,33,44,91,34,44]

for i in range(len(list)):
    for j in range(len(list)-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]

print(list)
print(list[-2])
 
# swap 2 numbers

a =10
b=20
a,b = b,a 
print(a,b)

temp =a
b =a
a=temp
print(a,b)


# missing no
numbers=[1,2,4,5]

n= len(numbers)+1  
sum1 = n*(n+1)//2

sum2 =sum(numbers)

missing_number = sum1 -sum2
print(missing_number)

