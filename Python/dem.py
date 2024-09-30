# n =13
# is_prime = True

# for i in range(2,n):
#     if n % i ==0:
#         print("its not a prime")
#         is_prime = False
#         break

# if(is_prime):
#     print("prime")


# for i in range(2,30+1):
#     is_prime = True
#     for j in range(2,i):
#         if i % j ==0 :
#             is_prime = False
#             break
#     if(is_prime):
#         print(i,"prime")


name = "maheshabdhjcbwiqengdyjesgcghnswoqwertyuioplkjgfdsazcxvbnmlpoiuytreqwasdfghjklmnbvcxzooiyeqsghlmo"

a = ""
for i in name:
    if i not in a:
        a += i
    else:
        a = a.replace(i,'')

print(a)