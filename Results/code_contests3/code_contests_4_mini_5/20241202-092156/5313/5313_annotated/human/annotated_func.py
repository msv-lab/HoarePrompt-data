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
        #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer; `x` is the integer square root of `n` where `x` squared is not equal to `n`. If `x * (x + 1) > n`, then `answr` is `4x + 2`. Otherwise, `answr` is `4 * (x + 1)`.
    #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer; `x` is the integer square root of `n`. If `x
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function accepts no parameters and reads an integer input `n` (where 1 ≤ n ≤ 10^6). It computes the integer square root `x` of `n` and determines a variable `answr` based on whether `n` is a perfect square or not. If `n` is a perfect square, it returns `4x`. If not, it checks if `x * (x + 1)` is greater than `n` to return `4x + 2`, otherwise it returns `4 * (x + 1)`. The result is then printed. Edge cases include the handling of perfect squares and values of `n` that are just above a square of an integer.

