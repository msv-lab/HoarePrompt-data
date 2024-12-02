#State of the program right berfore the function call: n is a non-negative integer.**
def func_1(n):
    count = 0
    for num in range(2, n):
        if is_prime(num):
            count += 1
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `count` is the number of prime numbers between 2 and `n` (inclusive), `num` is equal to or greater than `n`.
    return count
    #The program returns the number of prime numbers between 2 and `n` (inclusive).
#Overall this is what the function does:The function accepts a non-negative integer n and calculates the number of prime numbers between 2 and n (inclusive). It iterates through the range from 2 to n, checks if each number is prime using the `is_prime` function, and increments a count for each prime number found. The function then returns the count of prime numbers.

#State of the program right berfore the function call: num is a non-negative integer.**
def is_prime(num):
    if (num < 2) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: *num is a non-negative integer. num is greater than or equal to 2
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    #State of the program after the  for loop has been executed: If the loop executes, then `num` is a non-negative integer and a prime number, as the loop checks for divisibility from 2 to the square root of `num`. If the loop does not execute, `num` is a non-negative integer greater than or equal to 4 and is not divisible by any number from 2 to the square root of `num`.
    return True
    #The program returns True as the condition for the execution of the loop implies that `num` is a non-negative prime number.
#Overall this is what the function does:Functionality: The function `is_prime` accepts a non-negative integer parameter `num` and determines if it is a prime number. It returns False if `num` is less than 2 or if it is divisible by any number from 2 to the square root of `num`. If the loop does not execute, the function returns True, indicating that `num` is a non-negative prime number. The missing functionality in the annotations is handling the case where `num` is 2, which should return True since 2 is a prime number.

