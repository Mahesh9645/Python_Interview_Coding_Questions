# Sample Input 1 :
# 10
# Sample Output 1 :
# 1 2 5 10
# Explanation of Sample Input 1:
# The divisors of 10 are 1,2,5,10.


from typing import List
 
def printDivisors():  
    n= input()
    list = []
    for i in range(1,n+1):
        if n % i == 0:
            list.append(i) 
    return list 
