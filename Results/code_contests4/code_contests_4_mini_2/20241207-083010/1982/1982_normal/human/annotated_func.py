#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100000.
def func():
    n = int(input())
    i = '110'
    p = 1
    while int(i, 2) <= n:
        if n % int(i, 2) == 0:
            p = int(i, 2)
        
        i = '1' + i + '0'
        
    #State of the program after the loop has been executed: `n` is a positive integer such that 6 <= `n` <= 100000; `i` is a binary string formed by repeated concatenation of '1' at the start and '0' at the end, and `p` is the largest power of 2 less than or equal to `n` (if such a power exists). If no power of 2 less than or equal to `n` was found during the iterations, `p` remains 1.
    print(p)
#Overall this is what the function does:The function accepts a positive integer input `n` and calculates the largest power of 2 that is less than or equal to `n`, then prints this value. If no power of 2 is found that meets the criteria, it defaults to printing 1. The function does not return any value.

