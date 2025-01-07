#State of the program right berfore the function call: num is a positive integer such that 1 ≤ num ≤ 1000.
def func_1(num):
    if (num < 2) :
        return False
        #The program returns False as the value of num is less than 2
    #State of the program after the if block has been executed: *`num` is a positive integer such that 1 ≤ `num` ≤ 1000, and `num` is greater than or equal to 2.
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    #State of the program after the  for loop has been executed: `num` is a positive integer such that 1 ≤ `num` ≤ 1000, `num` is greater than or equal to 2, `i` has reached `int(num
    return True
    #The program returns True since 'num' is a positive integer greater than or equal to 2 and 'i' has reached 'int(num'
#Overall this is what the function does:The function accepts a positive integer `num` and returns `False` if `num` is less than 2 or if it is divisible by any integer from 2 up to the square root of `num`. If neither of these conditions are met, the function returns `True`, indicating that `num` is a prime number. However, the function does not handle the case where `num` is exactly 1, which is not prime but would return `True` due to the current implementation. Thus, the function does not accurately differentiate between prime and non-prime numbers for all valid inputs.

