#State of the program right berfore the function call: x is an integer such that 1 ≤ x ≤ 1000.
def func_1(x):
    if (x <= 1) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: x is an integer such that 1 < x ≤ 1000
    if (x <= 3) :
        return True
        #The program returns True
    #State of the program after the if block has been executed: x is an integer such that 1 < x ≤ 1000, and x is greater than 3
    if (x % 2 == 0 or x % 3 == 0) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: x is an integer such that 1 < x ≤ 1000, and x is greater than 3, and x is not divisible by 2 and x is not divisible by 3
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        
        i += 6
        
    #State of the program after the loop has been executed: `x` is an integer such that \(1 < x \leq 1000\), `x` is not divisible by 2 and 3, and \(x \geq 25\); `i` is the smallest number such that \((i + 6) * (i + 6) > x\).
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` accepts an integer `x` within the range of 1 to 1000. It returns `False` for all values of `x` except when `x` is 1000. For `x` = 1000, the function returns `True`. The function checks if `x` is less than or equal to 1, 3, or if `x` is divisible by 2 or 3, returning `False` in these cases. If none of these conditions are met, the function checks divisibility up to the square root of `x` using a while loop, returning `False` if `x` is divisible by any number of the form `i` or `i + 2` where `i` starts from 5 and increments by 6. If no divisors are found, the function returns `True`.

