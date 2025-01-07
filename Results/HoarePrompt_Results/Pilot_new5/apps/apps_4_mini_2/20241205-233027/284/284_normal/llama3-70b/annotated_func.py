#State of the program right berfore the function call: num is a positive integer such that 1 ≤ num ≤ 1000.
def func_1(num):
    if (num < 2) :
        return False
        #The program returns False since 'num' is a positive integer such that 1 ≤ 'num' ≤ 1000 and the current value of 'num' is less than 2.
    #State of the program after the if block has been executed: *`num` is a positive integer such that 1 ≤ `num` ≤ 1000, and `num` is greater than or equal to 2.
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    #State of the program after the  for loop has been executed: `num` is a positive integer such that 1 ≤ `num` ≤ 1000, `num` is a prime number, `i` is greater than or equal to 2 and less than or equal to `int(num
    return True
    #The program returns True, indicating that 'num' is a positive prime number within the range of 1 to 1000 and is evaluated with 'i' that is greater than or equal to 2 and less than or equal to int(num).
#Overall this is what the function does:The function accepts a positive integer `num` and returns `False` if `num` is less than 2 or if it is not a prime number; it returns `True` if `num` is a prime number between 1 and 1000. It does not explicitly check for even numbers except for the case where `num` is 2.

