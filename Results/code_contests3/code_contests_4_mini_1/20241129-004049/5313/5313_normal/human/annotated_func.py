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
        #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer; `x` is the integer part of the square root of `n` and is greater than 0. If `x * (x + 1)` is greater than `n`, then `answr` is calculated as (x + x + 1) * 2. Otherwise, `answr` is 4 * (x + 1).
    #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer; `x` is the integer part of the square root of `n`. If `x
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function accepts an integer input `n` (where 1 ≤ n ≤ 10^6) and calculates a value `answr` based on `n` and its integer square root `x`. If `n` is a perfect square, it returns `answr` as `4 * x`. If `n` is not a perfect square and `x * (x + 1)` is greater than `n`, it returns `answr` as `(x + x + 1) * 2`. Otherwise, it returns `answr` as `4 * (x + 1)`. The function prints the calculated `answr` but does not return it, which may lead to confusion since the description implies a return value that is not explicitly stated in the code.

