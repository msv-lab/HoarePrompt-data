#State of the program right berfore the function call: x is an integer such that 1 ≤ x ≤ 1000.
def func_1(x):
    if (x <= 1) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: x is an integer such that 1 ≤ x ≤ 1000, and x is greater than 1
    if (x <= 3) :
        return True
        #The program returns True
    #State of the program after the if block has been executed: x is an integer such that 1 ≤ x ≤ 1000, and x is greater than 3
    if (x % 2 == 0 or x % 3 == 0) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: x is an integer such that 1 ≤ x ≤ 1000, and x is greater than 3, and x is not divisible by 2 and x is not divisible by 3
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        
        i += 6
        
    #State of the program after the loop has been executed: `x` is an integer such that \(1 \leq x \leq 1000\), and \(x\) is greater than 3, and \(x\) is not divisible by 2 and not divisible by 3, and the function returns None if no divisors are found within the loop, otherwise it returns False. `i` is the smallest value such that \(i * i > x\).
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` accepts an integer `x` where \(1 \leq x \leq 1000\). It returns `True` if `x` is a prime number and `False` otherwise. Specifically:
- If `x` is less than or equal to 1, the function returns `False`.
- If `x` is 2 or 3, the function returns `True`.
- If `x` is divisible by 2 or 3, the function returns `False`.
- For other values of `x`, the function checks divisibility starting from 5 up to \(\sqrt{x}\) by incrementing by 6 each time, checking both `i` and `i+2`. If no divisors are found, the function returns `True`.

