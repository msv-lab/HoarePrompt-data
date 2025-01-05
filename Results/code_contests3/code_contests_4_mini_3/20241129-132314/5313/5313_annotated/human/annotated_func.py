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
        #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer; `x` is the integer part of the square root of `n`. If `x * (x + 1)` is greater than `n`, then `answr` is `4x + 2`. Otherwise, if `x * (x + 1)` is less than or equal to `n`, then `answr` is `4 * (x + 1)`.
    #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer; `x` is the integer part of the square root of `n`. If `x
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function accepts a positive integer input `n` (where 1 ≤ n ≤ 10^6) from the user and calculates a value based on the integer part of the square root of `n`, denoted as `x`. If `n` is a perfect square, it returns `4 * x`. If `x * (x + 1)` is greater than `n`, it returns `2 * (2 * x + 1)`. Otherwise, it returns `4 * (x + 1)`. The result is printed as an integer. The function does not return a value but outputs the result directly to the console.

