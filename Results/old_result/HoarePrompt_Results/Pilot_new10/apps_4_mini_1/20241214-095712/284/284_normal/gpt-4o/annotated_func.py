#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 1000.
def func_1(x):
    if (x <= 1) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 1000. `x` is greater than 1.
    if (x <= 3) :
        return True
        #The program returns True
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 1000, `x` is greater than 3.
    if (x % 2 == 0 or x % 3 == 0) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 1000, `x` is greater than 3, and `x` is neither divisible by 2 nor divisible by 3.
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        
        i += 6
        
    #State of the program after the loop has been executed: `i` is such that `i * i` is greater than `x`, `x` is a positive integer greater than or equal to `(i - 6) * (i - 6)`, `n` remains a positive integer such that 1 ≤ `n` ≤ 1000
    return True
    #The program returns True.
#Overall this is what the function does:The function accepts a positive integer `x` and determines if it is a prime number. It returns `False` if `x` is less than or equal to 1, or if it is divisible by 2 or 3. It also returns `False` if it has any divisors between 5 and the square root of `x` that are not multiples of 6 (i.e., checking for divisibility for numbers of the form 6k ± 1). If none of these conditions are met, it returns `True`, indicating that `x` is a prime number.

