#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and k is an integer such that 0 ≤ k ≤ (n * (n - 1)) / 2.
def func_1(n, k):
    if (k >= n - 1) :
        return 1
        #The program returns 1
    else :
        return n
        #The program returns an integer n such that 1 ≤ n ≤ 100
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, where `n` is an integer between 1 and 100, inclusive, and `k` is an integer between 0 and (n * (n - 1)) / 2, inclusive. If `k` is greater than or equal to `n - 1`, the function returns 1. Otherwise, it returns the value of `n`.

