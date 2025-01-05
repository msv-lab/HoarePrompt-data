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
        #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer; `x` is the integer value of the square root of `n`; the square of `x` is not equal to `n`. If `x * (x + 1)` is greater than `n`, then `answr` is assigned the value of (x + x + 1) * 2. Otherwise, `answr` is 4 * (x + 1).
    #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer; `x` is the integer value of the square root of `n`. If `x
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function accepts a positive integer input `n` (where 1 ≤ n ≤ 10^6) and calculates a value based on the integer square root of `n`. If `n` is a perfect square, it returns `4 * sqrt(n)`. If not, it assesses whether the sum of `x` and `x + 1` (where `x` is the integer square root of `n`) exceeds `n` to determine if it should return `(x + x + 1) * 2` or `4 * (x + 1)`. The function prints the final result, which is derived based on these calculations. Note that the function does not return any value; it only prints the result.

