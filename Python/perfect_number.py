# check number is perfect number or not

n =28
sum =0
for i in range(1,n):
    if n % i ==0:
        sum +=i
if n==sum:
    print("yes")

else :
    print("no")

# print 1 to 500 perfect numbers

a =1
b=500
# sum =0
for i in range(a,b+1):
    sum =0
    for j in range(1,i):
        if i % j == 0:
            sum +=j
    if (i ==sum):
        print(i,"perfect number")


# sum of digits

n =153
a = str(n)
s =0
for i in a:
    s = s + int(i)

print(s)

# length of string

print(len(a))

