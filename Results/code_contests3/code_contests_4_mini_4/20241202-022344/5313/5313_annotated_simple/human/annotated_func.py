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
        #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer within the same range; `x` is the integer part of the square root of `n`. If `x * (x + 1) > n`, then `answr` is calculated as (x + x + 1) * 2. Otherwise, `answr` is equal to `4 * (x + 1)`.
    #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer within the same range; `x` is the integer part of the square root of `n`. If `x
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function accepts no parameters and prompts the user to input a positive integer `n` (where 1 ≤ n ≤ 10^6). It calculates the integer part of the square root of `n` and determines an output value `answr` based on whether `n` is a perfect square or falls within certain conditions relative to the integer square root. The result is then printed to the console. Specifically, if `n` is a perfect square, it returns `4 * sqrt(n)`, if `x * (x + 1) > n`, it returns `2 * (x + x + 1)`, otherwise it returns `4 * (x + 1)`. The function does not return a value but prints the result directly.

