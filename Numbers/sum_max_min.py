def sum_maxi_number(numbers):
    """
    This function takes a list of numbers as input and returns the total sum,
    maximum number, and minimum number in the list.
    """
    total = 0  # Initialize the total sum
    max_number = numbers[0]  # Start with the first number as the maximum
    mini_number = numbers[0]  # Start with the first number as the minimum
    
    for i in numbers:
        total += i  # Add the current number to the total
        if i > max_number:  # Check for new maximum
            max_number = i
        elif i < mini_number:  # Check for new minimum
            mini_number = i
            
    return total, max_number, mini_number

# Example usage
numbers = [6, 2, 3, 4, 5, 6, 7]
result = sum_maxi_number(numbers)
print("Total Sum:", result[0])
print("Maximum Number:", result[1])
print("Minimum Number:", result[2])
