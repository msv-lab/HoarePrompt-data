#State of the program right berfore the function call: num is an integer such that 1 <= num <= 1000.
def func_1(num):
    if (num < 2) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: `num` is an integer such that 1 <= num <= 1000, and `num` is greater than or equal to 2
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    #State of the program after the  for loop has been executed: `num` is an integer such that \(1 \leq num \leq 1000\) and \(num \geq 2\), and if `num` is not a prime number, the function returns False. Otherwise, the function does not return anything (i.e., `num` remains unchanged and the function returns True).
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` accepts an integer `num` within the range of 1 to 1000. It checks whether `num` is a prime number by iterating from 2 to the square root of `num`. If `num` is divisible by any number in this range, the function returns `False`. If no divisors are found (i.e., `num` is not divisible by any number in the range), the function returns `True`. There are five possible outcomes: the function returns `False` if `num` is less than 2, if `num` is divisible by any number in the range [2, √num], or if `num` is less than 2 after the loop. The function returns `True` if `num` is a prime number and no divisors are found.

