#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 2 · 10^5.
def func_1(n):
    if (n == 0) :
        return -1
        #The program returns -1.
    #State: n is a positive integer such that 1 ≤ n ≤ 2 · 10^5, and n is not equal to 0.
    position = 0
    while n != 0:
        n >>= 1
        
        position += 1
        
    #State: position is the number of bits in the binary representation of the initial value of n, and n is 0.
    return position - 1
    #The program returns -1.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` (where 1 ≤ n ≤ 2 · 10^5) and returns the number of bits in the binary representation of `n` minus one. If `n` is 0, the function returns -1.

