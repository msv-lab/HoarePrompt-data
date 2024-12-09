#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    """Check if a number is prime."""
    if (n < 2) :
        return False
        #The program returns False since n is a non-negative integer and is less than 2.
    #State of the program after the if block has been executed: *`n` is a non-negative integer, and `n` is greater than or equal to 2.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer greater than or equal to 2, `i` is equal to `int(n
    return True
    #The program returns True
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns `False` if `n` is less than 2, or if `n` is divisible by any integer from 2 up to the square root of `n`. If `n` is greater than or equal to 2 and not divisible by any integer in that range, it returns `True`, indicating that `n` is a prime number.

#State of the program right berfore the function call: n is a positive integer such that n >= 1.
def func_2(n):
    """Find the nth Newman-Shanks-Williams prime number."""
    if (n == 1) :
        return 7
        #The program returns the value 7
    #State of the program after the if block has been executed: *`n` is a positive integer such that `n >= 1`, and `n` is greater than 1
    count = 1
    num = 7
    while True:
        if func_1(num):
            if num % 6 in [1, 5]:
                count += 1
                if count == n:
                    return num
        
        num += 1
        
    #State of the program after the loop has been executed: `n` is a positive integer such that `n >= 1` and `n > 1`, `count` is equal to `n`, `num` is the smallest integer greater than or equal to 7 such that `func_1(num)` returns true and `num % 6` is either 1 or 5.
#Overall this is what the function does:The function accepts a positive integer `n` and returns the nth Newman-Shanks-Williams prime number. If `n` is 1, it returns 7. For `n` greater than 1, it searches for the next prime numbers that are congruent to 1 or 5 modulo 6, and returns the nth such prime. This functionality implies that the function can potentially run indefinitely if there is an issue with `func_1`, as there is no exit condition in the loop besides finding the required prime.

