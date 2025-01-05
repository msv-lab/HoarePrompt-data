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
        #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer; `x` is the integer square root of `n` where `x` squared is not equal to `n`. If `x * (x + 1)` is greater than `n`, then `answr` is equal to `4x + 2`. Otherwise, `answr` is `4 * (x + 1)`.
    #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer; `x` is the integer square root of `n`. If `x
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function does not accept any parameters and reads an integer input `n` (1 ≤ n ≤ 10^6). It calculates an integer `x`, which is the integer square root of `n`. Based on the value of `n` and `x`, it determines a value `answr` which is printed as output. If `n` is a perfect square, `answr` is `4 * x`. If not, `answr` is `4 * (x + 1)` if `x * (x + 1) > n`, otherwise it is `4 * (x + 1)`. The function ultimately outputs the calculated value without any explicit return statement.

