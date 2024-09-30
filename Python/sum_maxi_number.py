def sum_maxi_number(numbers):
    total =0
    max_number = numbers[0]
    mini_number = numbers[0]
    for i in numbers:
        total += i
        if i > max_number:
            max_number = i
        elif i< mini_number:
            mini_number =i
    return total,max_number,mini_number

numbers = [6,2,3,4,5,6,7]
print(sum_maxi_number(numbers))


 