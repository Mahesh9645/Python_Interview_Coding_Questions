# number = int(input())
# fact_number =1
# for i in range(1,number+1):
#     fact_number =i*fact_number
#     # print(fact_number)

# print(fact_number)


n =2

fact_number  = 1

for i in range(1,n+1):
    fact_number *=i

print(fact_number)

# with def function


def  fact(n):
    if n==0:
        result =1
    else:
        result = n * fact(n-1)
    return result

print(fact(7))

