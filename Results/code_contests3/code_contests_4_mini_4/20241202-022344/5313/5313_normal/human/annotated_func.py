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
        #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ N ≤ 10^6; `n` is an input integer; `x` is the integer square root of `n`. If `x * (x + 1) > n`, then `answr` is `4x + 2`. Otherwise, `answr` is equal to `4 * (x + 1)`.
    #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer; `x` is the integer square root of `n`. If `x
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function accepts a positive integer `n` (input from the user) and calculates a value `answr` based on the integer square root of `n`. If `n` is a perfect square, it returns `4` times the square root of `n`. If it is not a perfect square and the product of the integer square root and one more than itself is greater than `n`, it returns `4` times the integer square root plus `2`. Otherwise, it returns `4` times one more than the integer square root. The output is printed directly and does not return a value.

