#State of the program right berfore the function call: x is an integer such that 1 <= x <= 1000.
def func_1(x):
    if (x <= 1) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: x is an integer such that 1 < x <= 1000
    if (x <= 3) :
        return True
        #The program returns True
    #State of the program after the if block has been executed: x is an integer such that 1 < x <= 1000, and x is greater than 3
    if (x % 2 == 0 or x % 3 == 0) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: x is an integer such that 1 < x <= 1000, and x is greater than 3, and x is not divisible by 2 and x is not divisible by 3
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        
        i += 6
        
    #State of the program after the loop has been executed: `x` is an integer such that \(25 \leq x \leq 1000\), and \(x > 3\), and \(x\) is not divisible by 2 and \(x\) is not divisible by 3, and \(x \mod 5 \neq 0\), and \(x \mod 7 \neq 0\), and \(x\) is a prime number greater than or equal to 25; `i` is increased by 6 after the loop has finished
    return True
    #The program returns True
#Overall this is what the function does:The function accepts an integer `x` in the range \(1 \leq x \leq 1000\) and returns `False` if `x` is 1, 2, 3, or divisible by 2 or 3. For other values, it returns `True` if `x` is a prime number greater than or equal to 25.

