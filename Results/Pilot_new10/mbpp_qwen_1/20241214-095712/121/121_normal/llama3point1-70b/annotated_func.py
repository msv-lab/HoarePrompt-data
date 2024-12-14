#State of the program right berfore the function call: n is a non-negative integer representing the position of the Newman–Shanks–Williams prime number to be found.
def func_1(n):
    """Check if a number is prime."""
    if (n < 2) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: *n is a non-negative integer representing the position of the Newman–Shanks–Williams prime number to be found, and n is greater than or equal to 2
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer representing the position of the Newman–Shanks–Williams prime number to be found, and either the function returns `False` (if `n` is not a prime number) or `i` exceeds the integer value of `n` (if `n` is a prime number).
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and returns `False` if `n` is less than 2 or if `n` is divisible by any integer from 2 to the square root of `n`. If none of these conditions are met, the function returns `True`, indicating that `n` is a prime number.

#State of the program right berfore the function call: n is a positive integer (1 <= n).
def func_2(n):
    """Find the nth Newman-Shanks-Williams prime number."""
    if (n == 1) :
        return 7
        #The program returns 7
    #State of the program after the if block has been executed: `n` is a positive integer (1 <= n), the code to find the nth Newman-Shanks-Williams prime number has been initiated, and `n` is not equal to 1
    count = 1
    num = 7
    while True:
        if func_1(num):
            if num % 6 in [1, 5]:
                count += 1
                if count == n:
                    return num
        
        num += 1
        
    #State of the program after the loop has been executed: `n` is a positive integer (1 <= n) and not equal to 1; `count` is `n`; `num` is `6*n + 1` or `6*n + 5`; the function `func_1(num)` evaluates to True if the number `num` is either 1 more than a multiple of 6 or 5 more than a multiple of 6.
#Overall this is what the function does:The function accepts a positive integer `n` and returns the nth Newman-Shanks-Williams prime number. If `n` is 1, it returns 7. For other values of `n`, it starts with `num` set to 7 and increments `num` until it finds a number that satisfies the conditions of being 1 more or 5 more than a multiple of 6 and is a prime number according to `func_1(num)`. Once such a number is found and it matches the required count, it returns that number.

