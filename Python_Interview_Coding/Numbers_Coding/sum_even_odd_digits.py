# Given string of objects  find the sum of all possiable given digits      company name :zoho
num = 1546827
even_sum = 0
odd_sum = 0
odd_list = []

for i in str(num):  # Convert the number to a string to loop through each digit
    if int(i) % 2 != 0:  # If the digit is odd
        odd_list.append(int(i))  # Add the odd digit to the odd_list
        odd_sum += int(i)  # Add the odd digit to the odd_sum
    else:  # If the digit is even
        even_sum += int(i)  # Add the even digit to the even_sum


print(f'Even sum: {even_sum}')
print(f'Odd sum: {odd_sum}')
print(f'Odd digits: {odd_list}')

print(odd_list)

