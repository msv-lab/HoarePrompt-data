#State of the program right berfore the function call: num is an integer such that 1 ≤ num ≤ 1000.
def func_1(num):
    if (num < 2) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: num is an integer such that 2 ≤ num ≤ 1000.
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    #State of the program after the  for loop has been executed: `num` is an integer such that 2 ≤ num ≤ 1000, `i` is `int(num
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` accepts an integer `num` (1 ≤ num ≤ 1000) and returns `True` if `num` is a prime number; otherwise, it returns `False`. If `num` is less than 2, the function immediately returns `False`. For numbers greater than or equal to 2, the function checks if `num` is divisible by any integer from 2 up to the square root of `num`. If any such divisor is found, the function returns `False`; otherwise, it returns `True`. The final state of the program is that the function has determined whether the input `num` is a prime number and returned the corresponding boolean value.

