#State of the program right berfore the function call: n is a non-negative integer, where n represents the number to be checked for primality and must be greater than or equal to 0.
def func_1(n):
    """Check if a number is prime."""
    if (n < 2) :
        return False
        #The program returns False because n is a non-negative integer less than 2, which is not prime.
    #State of the program after the if block has been executed: *`n` is a non-negative integer, where `n` represents the number to be checked for primality and must be greater than or equal to 2.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer greater than or equal to 2, `i` is `int(n
    return True
    #The program returns True
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns False if `n` is less than 2, indicating that it is not a prime number. If `n` is greater than or equal to 2, the function checks for divisibility by all integers from 2 up to the square root of `n`. If `n` is divisible by any of these integers, it returns False, implying that `n` is not prime. If `n` is not divisible by any of these integers, it returns True, indicating that `n` is a prime number. The function does not clearly handle negative inputs for its postconditions, but those cases are effectively excluded by the primary input requirement of non-negative integers.

#State of the program right berfore the function call: n is a positive integer representing the position of the Newman-Shanks-Williams prime number to find, with n >= 1.
def func_2(n):
    """Find the nth Newman-Shanks-Williams prime number."""
    if (n == 1) :
        return 7
        #The program returns the Newman-Shanks-Williams prime number at position 1, which is 7.
    #State of the program after the if block has been executed: *`n` is a positive integer representing the position of the Newman-Shanks-Williams prime number to find, with `n >= 1`. The value of `n` is greater than 1.
    count = 1
    num = 7
    while True:
        if func_1(num):
            if num % 6 in [1, 5]:
                count += 1
                if count == n:
                    return num
        
        num += 1
        
    #State of the program after the loop has been executed: `n` is a positive integer greater than 1; `count` is 3; `num` is 11; if `func_1(num)` returns true for `num` values 8, 9, and 10, then `count` will have reached `n` once `num` becomes 11.
#Overall this is what the function does:The function accepts a positive integer `n` representing the position of the Newman-Shanks-Williams prime number to find. It returns 7 if `n` is 1. For values of `n` greater than 1, it returns the nth Newman-Shanks-Williams prime number, which may be any prime number greater than 7 that satisfies the conditions checked in the loop. The function relies on an undefined `func_1` to determine primality and checks that prime numbers are of the form 6k ± 1. The potential for infinite looping exists if `func_1` never returns true or if the conditions to increment `count` are not met.

