n = 12345892345678861
while len(str(n)) > 1:  # Continue until the number becomes a single digit
    sum_digits = 0
    for digit in str(n):  # Iterate over each digit in the number
        sum_digits += int(digit)  # Convert each character to an integer and sum it
    n = sum_digits  # Update n to be the sum of the digits
print(n)  # Output the result