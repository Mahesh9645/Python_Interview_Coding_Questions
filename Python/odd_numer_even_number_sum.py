number_str = str(input()) 
even_sum = 0
odd_sum = 0

# for i in number_str:
#     i = int(i)
#     if i % 2 == 0:
#         even_sum += i
#     else:   
#         odd_sum += i

# print(even_sum,odd_sum)
 

# Calculating sums using list comprehensions
even_sum = sum(int(num) for num in number_str if int(num) % 2 == 0)
odd_sum = sum(int(num) for num in number_str if int(num) % 2 != 0)

print(even_sum, odd_sum)