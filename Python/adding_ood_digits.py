# Given string of objects  find the sum of all possiable given digits      company name :zoho
num = 1546827
a = str(num)
b = len(a)
even_sum =0
odd_sum =0
odd_list = []
for i in a:
    if int(i) % 2 !=0:
        odd_list.append(int(i))
        odd_sum += int(i)
    else:
        print(int(i))
        even_sum = even_sum+int(i)

print(f'even_sum : {even_sum}')
print(f'even_sum : {odd_sum}')
print(odd_list)

