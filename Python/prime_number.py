# check no. is prime or not

n =13
is_prime = True
for i in range(2,n):
    if n%i ==0:
        is_prime = False
        print("its not a prime number")
        break
if is_prime:
    print("its a prime number")


#  print prime number between 2 to50

for i in range(2,51):
    is_prime = True
    for j in range(2,i):
        if i % j ==0:
            is_prime =False
            break
    if is_prime:
        print(i)

# for i in range(2, 51):
#     is_prime = True
#     for j in range(2, i):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(i)
