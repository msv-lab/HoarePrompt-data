#State of the program right berfore the function call: num is a positive integer such that 1 ≤ num ≤ 1000.
def func_1(num):
    if (num < 2) :
        return False
        #The program returns False because the current value of `num` is less than 2, and it is specified that `num` is a positive integer such that 1 ≤ `num` ≤ 1000.
    #State of the program after the if block has been executed: *`num` is a positive integer such that 1 ≤ `num` ≤ 1000, and `num` is greater than or equal to 2.
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    #State of the program after the  for loop has been executed: `num` is a positive integer such that 2 ≤ `num` ≤ 1000 and is a prime number, `i` is equal to `int(num
    return True
    #The program returns True, confirming that 'num' is a positive integer within the range of 2 to 1000 and is a prime number.
#Overall this is what the function does:The function accepts a positive integer `num` within the range 1 to 1000 and returns False if `num` is less than 2 or if it is divisible by any integer between 2 and the square root of `num`. If `num` is greater than or equal to 2 and not divisible by any of those integers, it returns True, indicating that `num` is a prime number.

