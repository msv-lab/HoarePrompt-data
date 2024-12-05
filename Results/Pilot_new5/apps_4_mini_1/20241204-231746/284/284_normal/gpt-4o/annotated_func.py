#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 1000.
def func_1(x):
    if (x <= 1) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 1000, and `x` is greater than 1.
    if (x <= 3) :
        return True
        #The program returns True
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 1000, and `x` is greater than 3.
    if (x % 2 == 0 or x % 3 == 0) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 1000, `x` is greater than 3, and `x` is neither divisible by 2 nor divisible by 3.
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        
        i += 6
        
    #State of the program after the loop has been executed: `i` is greater than the square root of `x`, `x` is original and unaltered, `n` is a positive integer such that 1 ≤ `n` ≤ 1000, and if the loop terminated without returning False, `x` is a prime number greater than 3 that is not divisible by 2 or 3.
    return True
    #The program returns True, indicating that x is a prime number greater than 3 that is not divisible by 2 or 3.
#Overall this is what the function does:The function accepts a positive integer `x` and checks if it is a prime number. It returns False if `x` is less than or equal to 1, or if `x` is even or divisible by 3 (except for 2 and 3 themselves). If `x` is greater than 3 and passes these checks, it further verifies that it is not divisible by any integers up to its square root. If all checks are passed, it returns True, indicating that `x` is a prime number; otherwise, it returns False. Additionally, the function does not handle the special case of `x` being 2 or 3 explicitly, which should return True as they are prime numbers.

