#State of the program right berfore the function call: n is an integer greater than 1.
def func_1(n):
    if (n <= 1) :
        return True
        #The program returns True
    #State of the program after the if block has been executed: n is an integer greater than 1, and n is greater than 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return True
        
    #State of the program after the  for loop has been executed: `n` is an integer greater than 1, and the function does not return `True` if no `i` in the range [2, int(math.sqrt(n))] divides `n` evenly.
    return False
    #The program returns False
#Overall this is what the function does:The function `func_1` accepts an integer `n` and returns a boolean value. If `n` is less than or equal to 1, the function returns `True`. For integers `n` greater than 1, the function returns `True` if `n` is divisible by any integer `i` in the range [2, int(sqrt(n))]. If no such `i` exists, the function returns `False`. In essence, the function returns `False` only if `n` is a prime number greater than 1; otherwise, it returns `True`.

