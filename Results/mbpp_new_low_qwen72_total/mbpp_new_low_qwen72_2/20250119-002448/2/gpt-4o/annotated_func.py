#State of the program right berfore the function call: n is an integer greater than 1.
def func_1(n):
    if (n <= 1) :
        return True
        #The program returns True
    #State of the program after the if block has been executed: *n is an integer greater than 1, and n is greater than 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return True
        
    #State of the program after the  for loop has been executed: `n` is an integer greater than 1, `i` is `int(math.sqrt(n)) + 1`, and the function returns `True` if `n` is not a prime number; otherwise, it returns `None`.
    return False
    #The program returns False
#Overall this is what the function does:The function `func_1` accepts an integer `n` greater than 1. It returns `True` if `n` is not a prime number, and `False` if `n` is a prime number. If `n` is less than or equal to 1, the function immediately returns `True`. The final state of the program after the function concludes is that the function has returned either `True` or `False` based on whether `n` is a non-prime or prime number, respectively.

