#State of the program right berfore the function call: x is a positive integer such that 1 ≤ x ≤ 1000.
def func_1(x):
    if (x <= 1) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: x is a positive integer such that 1 ≤ x ≤ 1000, and x is greater than 1
    if (x <= 3) :
        return True
        #The program returns boolean value True
    #State of the program after the if block has been executed: x is a positive integer such that 1 ≤ x ≤ 1000, and x is greater than 1, and x is greater than 3
    if (x % 2 == 0 or x % 3 == 0) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: x is a positive integer such that 4 ≤ x ≤ 1000, x is greater than 1, x is greater than 3, and x is neither divisible by 2 nor by 3.
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        
        i += 6
        
    #State of the program after the loop has been executed: `i` is `35` (since it increments to this value right after the last valid iteration where `i` squared is less than or equal to `x`, considering the loop stops when `i` squared exceeds `x`), and `x` remains unchanged if it is not divisible by any of the primes less than or equal to the square root of `x`, meaning `x` is a prime number itself within the given range if it passes all the divisibility checks without returning `False`.
    return True
    #The program returns True, indicating that the number `x` has passed all divisibility checks and is likely a prime number, with `i` being 35, which is the value it incremented to after the last valid iteration where `i` squared was less than or equal to `x`.
#Overall this is what the function does:The function checks if a given integer `x`, where `1 ≤ x ≤ 1000`, is likely a prime number and returns a boolean value indicating whether `x` is prime or not, with specific optimizations for divisibility checks.

