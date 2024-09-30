"""An Armstrong number (or Narcissistic number) is a number that is equal to the sum of its own 
digits each raised to the power of the number of digits."""

print(__doc__)
n = 9474  # The number to check

# Get the number of digits in the number
pow = len(str(n))

sum = 0  # Initialize sum to 0
for digits in str(n):  # Loop through each digit in the number
    sum += int(digits) ** pow  # Add each digit raised to the power of the number of digits

# Check if the sum equals the original number
print(sum == n)  # True if it's an Armstrong number, False otherwise

# Print the number of digits in the number
print(len(str(n)))  # Output the number of digits