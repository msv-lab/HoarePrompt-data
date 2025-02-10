#State of the program right berfore the function call: n is an integer where 1 ≤ n ≤ 100, and k is an integer where 0 ≤ k ≤ n * (n - 1) / 2.
def func_1(n, k):
    if (k >= n - 1) :
        return 1
        #The program returns 1.
    else :
        return n
        #The program returns the integer value of n, where 1 ≤ n ≤ 100.
#Overall this is what the function does:The function `func_1` takes two parameters, `n` and `k`, where `n` is an integer in the range 1 to 100, and `k` is an integer in the range 0 to n * (n - 1) / 2. If `k` is greater than or equal to `n - 1`, the function returns 1. Otherwise, it returns the value of `n`.

