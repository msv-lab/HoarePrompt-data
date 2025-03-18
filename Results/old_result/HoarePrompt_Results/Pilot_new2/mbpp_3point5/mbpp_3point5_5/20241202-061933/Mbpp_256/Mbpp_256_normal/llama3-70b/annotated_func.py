#State of the program right berfore the function call: n is a non-negative integer.**
def func_1(n):
    count = 0
    for num in range(2, n):
        if is_prime(num):
            count += 1
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `count` is the number of prime numbers between 2 and `n`, `num` is `n`. If `num` is a prime number, then the function increments `count` by 1.
    return count
    #The program returns the number of prime numbers between 2 and `n`, where `n` is a non-negative integer, and `count` is the count of prime numbers
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and calculates the number of prime numbers between 2 and `n`. The function iterates through numbers from 2 to `n` (exclusive) and checks if each number is prime using the `is_prime` function. It then returns the count of prime numbers found within the specified range. The code does not consider the case where `n` is less than 2, which would lead to an incorrect count of prime numbers. Additionally, the function does not handle the scenario where `n` is equal to 2, resulting in a count of prime numbers being 0 when it should be 1.

#State of the program right berfore the function call: num is a non-negative integer.**
def is_prime(num):
    if (num < 2) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: *num is a non-negative integer. num is greater than or equal to 2.
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    #State of the program after the  for loop has been executed: `num` is a non-negative integer and greater than or equal to 2. The loop iterates through all numbers from 2 to the square root of `num` (inclusive). For each `i`, if `num` is divisible by `i`, the function returns False. If `num` is not divisible by any `i`, the function does not return anything.
    return True
    #The function returns True if the non-negative integer 'num' is not divisible by any number from 2 to the square root of 'num' (inclusive).
#Overall this is what the function does:The function `is_prime` accepts a non-negative integer `num` and determines if it is a prime number. It checks if `num` is less than 2 and returns False in that case. Then, it iterates through numbers from 2 to the square root of `num` and returns False if `num` is divisible by any of these numbers. Finally, it returns True if `num` is not divisible by any number from 2 to the square root of `num` (inclusive). The function accurately determines whether the input `num` is a prime number by checking for divisibility.

