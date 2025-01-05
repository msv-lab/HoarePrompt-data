#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 106.**
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
        #State of the program after the if-else block has been executed: *`N` is an integer such that 1 ≤ N ≤ 106; `x` is an integer. x is not a square root of n. If x * (x + 1) > n, `answr` is calculated as 4x + 2. If x * (x + 1) is less than or equal to n, `answr` is calculated as 4 * (x + 1).
    #State of the program after the if-else block has been executed: *`N` is an integer such that 1 ≤ N ≤ 106; `x` is an integer. If the square of `x` is equal to `n`, then `answr` is equal to `4 * sqrt(n)`. If `x` is not a square root of `n`, and if x * (x + 1) > n, then `answr` is calculated as 4x + 2. If x * (x + 1) is less than or equal to n, then `answr` is calculated as 4 * (x + 1).
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function `func` reads an integer `n` from the user input, calculates a value `x` based on the square root of `n`, and then determines the value of `answr` based on different conditions. If the square of `x` is equal to `n`, `answr` is set to `4 * sqrt(n)`. If `x` is not a square root of `n`, and if `x * (x + 1) > n`, then `answr` is calculated as `4x + 2`. If `x * (x + 1)` is less than or equal to `n`, then `answr` is calculated as `4 * (x + 1)`. The final value of `answr` is printed as an integer. The function does not explicitly return any value.

