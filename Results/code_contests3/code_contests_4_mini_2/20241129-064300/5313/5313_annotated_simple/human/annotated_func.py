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
        #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer; `x` is the integer part of the square root of `n`. If `x * (x + 1) > n`, then `answr` is calculated as 4x + 2. Otherwise, `answr` is calculated as 4 * (x + 1).
    #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 10^6; `n` is an input integer; `x` is the integer part of the square root of `n`. If `x
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function accepts no parameters and reads a positive integer `n` from the input, where 1 ≤ `n` ≤ 10^6. It calculates an integer value `answr` based on whether `n` is a perfect square or if `x * (x + 1)` exceeds `n`. It prints `answr`, which is calculated as follows: if `n` is a perfect square, it returns `4 * sqrt(n)`, otherwise it checks if `x * (x + 1) > n` and returns `2 * (x + x + 1)`, or `4 * (x + 1)` if not. The function does not return a value but prints the result instead. Additionally, if the input is out of range, the behavior is undefined since no validation is provided for the input value.

