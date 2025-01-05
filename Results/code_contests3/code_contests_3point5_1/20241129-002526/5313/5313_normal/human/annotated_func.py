#State of the program right berfore the function call: N is a positive integer such that 1 <= N <= 10^6.**
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
        #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 <= N <= 10^6, `x` is the integer square root of `N`. If `x * (x + 1) > N`, then `answr` is the result of the calculation. Otherwise, `answr` is 4 times the sum of the integer square root of `N` and 1.
    #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 <= N <= 10^6, `x` is the integer square root of `N`. If the square of `x` is equal to `N`, then `answr` is equal to `N * 4`. If `x * (x + 1) > N`, then `answr` is the result of the calculation. Otherwise, `answr` is 4 times the sum of the integer square root of `N` and 1.
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function `func` reads an integer `n` from the user input, calculates the integer square root `x` of `n`, and based on certain conditions, computes a value for `answr`. If the square of `x` is equal to `n`, `answr` is set to `n * 4`. If `x * (x + 1) > n`, `answr` is calculated accordingly. Otherwise, `answr` is set to 4 times the sum of `x` and 1. The final value of `answr` is then converted to an integer and printed. The function does not have any specified return value.

