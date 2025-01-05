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
        #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer; `x` is the integer part of the square root of `n`. If `x * (x + 1) > n`, then `answr` is calculated as (x + x + 1) * 2. Otherwise, `answr` is calculated as 4 * (x + 1).
    #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer; `x` is the integer part of the square root of `n`. If `x
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function accepts a positive integer input `n`, computes its integer square root `x`, and depending on the value of `n`, calculates and prints a specific value `answr`. If `n` is a perfect square, it returns `4 * x`. If `n` is not a perfect square and `x * (x + 1) > n`, it returns `(x + x + 1) * 2`. Otherwise, it returns `4 * (x + 1)`. The function does not have any return statement but prints the result instead.

