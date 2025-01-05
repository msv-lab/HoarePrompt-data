#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 10^6.
def func():
    n = int(input())
    x = int(n ** 0.5)
    if (x ** 2 == n) :
        answr = x * 4
    else :
        if (x * (x + 1) > n) :
            answr = (x + x + 1) * 2
        else :
            answr = 4 * (x + 1)
        #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer; `x` is the integer part of the square root of `n` where `x` squared is not equal to `n`. If `x * (x + 1)` is greater than `n`, then `answr` is `4x + 2`. Otherwise, `answr` is `4 * (x + 1)`.
    #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer; `x` is the integer part of the square root of `n`. If `x^2 = n`, then `answr` is equal to `4 * x`. If `x^2` is not equal to `n`, and if `x * (x + 1)` is greater than `n`, then `answr` is `4x + 2`; otherwise, `answr` is `4 * (x + 1)`.
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function accepts a positive integer input `n` (where 1 ≤ n ≤ 10^6) and calculates a value `answr` based on whether `n` is a perfect square or not. If `n` is a perfect square, it returns `4 * x`, where `x` is the integer part of the square root of `n`. If `n` is not a perfect square and `x * (x + 1)` is greater than `n`, it returns `4 * x + 2`; otherwise, it returns `4 * (x + 1)`. The function does not return a value but instead prints the computed result.

