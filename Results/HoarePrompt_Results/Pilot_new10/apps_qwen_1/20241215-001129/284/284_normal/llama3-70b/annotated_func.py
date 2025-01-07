#State of the program right berfore the function call: num is an integer such that 1 ≤ num ≤ 1000.
def func_1(num):
    if (num < 2) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: num is an integer such that 1 ≤ num ≤ 1000, and num is greater than or equal to 2
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    #State of the program after the  for loop has been executed: `num` is an integer such that \(1 \leq num \leq 1000\) and `num` is greater than or equal to 2, `i` is `int(num
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` accepts an integer `num` within the range of 1 to 1000 and returns `True` if `num` is a prime number. It returns `False` if `num` is less than 2 or if `num` is divisible by any integer from 2 to the square root of `num`.

