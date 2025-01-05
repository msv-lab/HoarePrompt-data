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
        #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer; `x` is the integer square root of `n`. If `x * (x + 1) > n`, then `answr` is calculated as `4x + 2`. Otherwise, `answr` is calculated as `4 * (x + 1)`.
    #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer; `x` is the integer square root of `n`. If `x
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function accepts an integer input `n` (which must be a positive integer between 1 and 10^6) and calculates a value `answr` based on the integer square root `x` of `n`. If `n` is a perfect square, it returns `4 * x`. If not, it checks whether `x * (x + 1)` is greater than `n`. If it is, it returns `2 * (2x + 1)`, otherwise, it returns `4 * (x + 1)`. The function prints the value of `answr`. It does not return any values explicitly, only prints the result.

