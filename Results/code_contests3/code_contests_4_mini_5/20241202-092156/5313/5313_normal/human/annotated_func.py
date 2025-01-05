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
        #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer; `x` is the integer square root of `n` and it is not true that `x` is an integer. If `x * (x + 1)` is greater than `n`, then `answr` is set to `4x + 2`. Otherwise, `answr` is set to `4 * (x + 1)`.
    #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer; `x` is the integer square root of `n`. If `x
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function accepts an integer input `n` (where `1 ≤ n ≤ 10^6`) and calculates a value `answr` based on the integer square root `x` of `n`. If `x` is an integer square root of `n`, it sets `answr` to `4 * x`. If not, it checks if `x * (x + 1)` exceeds `n`, setting `answr` to `4 * x + 2` if true; otherwise, it sets `answr` to `4 * (x + 1)`. Finally, it prints the value of `answr`.

