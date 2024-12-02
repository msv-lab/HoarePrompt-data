#State of the program right berfore the function call: n is a non-negative integer.**
def func_1(n):
    count = 0
    for num in range(2, n):
        if is_prime(num):
            count += 1
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `count` is the number of prime numbers between 2 and `n` (exclusive)
    return count
    #The program returns the number of prime numbers between 2 and `n` (exclusive) as `count`
#Overall this is what the function does:The function accepts a non-negative integer n and calculates the count of prime numbers between 2 and n (exclusive) as count. It iterates through the numbers from 2 to n, excluding n, and increments count for each prime number found. The function then returns the final count of prime numbers.

#State of the program right berfore the function call: num is a non-negative integer.**
def is_prime(num):
    if (num < 2) :
        return False
        #The program returns False when num is a non-negative integer less than 2
    #State of the program after the if block has been executed: *num is a non-negative integer. num is greater than or equal to 2
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    #State of the program after the  for loop has been executed: If the loop executes, then `num` is a non-negative integer greater than or equal to 2 and is a prime number. If the loop does not execute, then `num` is a non-negative integer greater than or equal to 2 and is not a prime number.
    return True
    #The program returns True
#Overall this is what the function does:The function `is_prime` accepts a non-negative integer `num` and determines if it is a prime number. It returns False if `num` is less than 2 or divisible by 2 without a remainder. If `num` is greater than or equal to 2 and not divisible by any number from 2 to the square root of `num`, it returns True.

