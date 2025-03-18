#State of the program right berfore the function call: n is a non-negative integer.**
def func_1(n):
    count = 0
    for num in range(2, n):
        if is_prime(num):
            count += 1
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `count` is the number of prime numbers between 2 and `n`, `num` is `n` - 1. The variable `count` is incremented by 1 for each prime number found during the loop execution.
    return count
    #The program returns the number of prime numbers between 2 and 'n', where 'n' is a non-negative integer
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and calculates the number of prime numbers between 2 and n. It iterates through the numbers from 2 to n-1, incrementing a count variable for each prime number found. The function then returns the total count of prime numbers. However, the code does not include a check for when n is less than 2, which could be considered to handle edge cases where n is 0 or 1.

#State of the program right berfore the function call: num is a non-negative integer.**
def is_prime(num):
    if (num < 2) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: *num is a non-negative integer. num is larger than or equal to 2
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    #State of the program after the  for loop has been executed: If the loop executes, then `num` is a prime number, as it is not divisible by any number from 2 to the square root of `num`. If the loop does not execute, then `num` is a prime number as well, since the condition for the loop to execute is that `num` is not divisible by any number from 2 to the square root of `num`.
    return True
    #The program returns True, indicating that `num` is a prime number
#Overall this is what the function does:The function `is_prime` accepts a non-negative integer `num` and determines if it is a prime number. If `num` is less than 2, the function returns False. If `num` is divisible by any number from 2 to the square root of `num`, the function returns False. If `num` is not divisible by 2 and is not divisible by 3, the function returns False. Otherwise, if none of the previous conditions are met, the function returns True, indicating that `num` is a prime number.

