# Input list of numbers
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Initialize two lists to store even and odd numbers
even_numbers = []
odd_numbers = []

# Loop through the list to separate even and odd numbers
for num in list2:
    if num % 2 == 0:  # Check if the number is even
        even_numbers.append(num)
    else:             # Otherwise, it is odd
        odd_numbers.append(num)

# Print the even and odd numbers
print(f'Even numbers are: {even_numbers}')
print(f'Odd numbers are: {odd_numbers}')

# Alternative one-liner to calculate the sum of even and odd numbers
even_sum = sum([i for i in list2 if i % 2 == 0])
odd_sum = sum([i for i in list2 if i % 2 != 0])

# Print the sums of even and odd numbers
print(f'Sum of even numbers: {even_sum}')
print(f'Sum of odd numbers: {odd_sum}')
