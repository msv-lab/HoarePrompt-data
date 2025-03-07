#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 2 \cdot 10^5.
def func_1(n):
    return sum(int(d) for d in str(n))
    #The program returns the sum of the digits of the positive integer `n` where 1 <= n <= 200000.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` where 1 <= n <= 200000 and returns the sum of its digits. After the function concludes, the input integer `n` remains unchanged, and the returned value is the sum of the digits of `n`.

