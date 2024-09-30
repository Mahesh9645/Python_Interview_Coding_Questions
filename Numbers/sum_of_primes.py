# Initialize the sum of prime numbers
prime_sum = 0

# Loop through numbers from 2 to 10
for i in range(2, 11):
    is_prime = True  # Assume the number is prime initially
    # Check for factors from 2 to i-1
    for j in range(2, i):
        if i % j == 0:  # If i is divisible by j, it's not prime
            is_prime = False
            break  # Exit the inner loop if a factor is found
    if is_prime:  # If the number is prime
        print(i)  # Print the prime number
        prime_sum += i  # Add the prime number to the sum

# Print the sum of prime numbers found
print("Sum of primes:", prime_sum)
