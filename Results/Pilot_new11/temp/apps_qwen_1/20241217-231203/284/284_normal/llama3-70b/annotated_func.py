#State of the program right berfore the function call: num is an integer such that 1 ≤ num ≤ 1000.
def func_1(num):
    if (num < 2) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: num is an integer such that 1 ≤ num ≤ 1000, and num is greater than or equal to 2
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    #State of the program after the  for loop has been executed: `num` is an integer such that \(1 \leq num \leq 1000\) and `num` is either prime or not divisible by any integer `i` in the range \([2, \lfloor \sqrt{num} \rfloor + 1]\). If `num` is found to be divisible by any integer `i` in this range during the loop, the function returns `False`. Otherwise, the function completes and `num` remains unchanged.
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` accepts an integer `num` as input, where `1 ≤ num ≤ 1000`. It checks whether `num` is a prime number. The function returns `False` if `num` is less than 2 or if `num` is divisible by any integer `i` in the range `[2, √num]`. If `num` is not divisible by any integer in this range, the function returns `True`, indicating that `num` is a prime number.

