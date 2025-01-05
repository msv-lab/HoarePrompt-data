#State of the program right berfore the function call: N is an integer such that 1 <= N <= 10^6.**
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
        #State of the program after the if-else block has been executed: *N is an integer such that 1 <= N <= 10^6; `n` is an input integer, `x` is the integer square root of `n`, `answr` is an integer. If x * (x + 1) > n, `answr` is an integer greater than or equal to 6. Otherwise, `answr` is 4 times the next integer after `x`.
    #State of the program after the if-else block has been executed: *N is an integer such that 1 <= N <= 10^6; n is an input integer, x is the integer square root of n. If x^2 = n, answr is 4 times the integer square root of n. If x * (x + 1) > n, answr is an integer greater than or equal to 6. Otherwise, answr is 4 times the next integer after x.
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function `func` reads an integer input `n`, calculates the integer square root `x` of `n`, and determines the value of `answr` based on specific conditions. If `x` squared equals `n`, `answr` is set to 4 times `x`. If `x` multiplied by `x + 1` is greater than `n`, `answr` is set to 2 times `x + 1`. Otherwise, `answr` is set to 4 times the next integer after `x`. The final value of `answr` is then printed as an integer.

