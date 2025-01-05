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
        #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer; `x` is the integer part of the square root of `n`, which is not a perfect square. If `x * (x + 1) > n`, then `answr` is `4x + 2`. Otherwise, `answr` is calculated as `4 * (x + 1)`.
    #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; if `n` is a perfect square, then `answr` is equal to `x * 4`, where `x` is the integer square root of `n`. If `n` is not a perfect square and if `x * (x + 1) > n`, then `answr` is `4x + 2`; otherwise, `answr` is calculated as `4 * (x + 1)`.
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function accepts a positive integer `n` (input by the user) and calculates a value `answr` based on the integer part of the square root of `n`. If `n` is a perfect square, it returns `4 * x`, where `x` is the integer square root of `n`. If `n` is not a perfect square and `x * (x + 1) > n`, it returns `4 * x + 2`. Otherwise, it returns `4 * (x + 1)`. Finally, it prints the computed value `answr`. The function does not return any value, and its output is directly printed.

