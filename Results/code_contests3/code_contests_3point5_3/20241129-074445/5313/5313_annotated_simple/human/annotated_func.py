#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 10^6.**
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
        #State of the program after the if-else block has been executed: *N is an integer such that 1 ≤ N ≤ 10^6, n is an input integer, x is the square root of n, and the square of x is not equal to n. If x * (x + 1) > n, answr is calculated based on certain conditions. Otherwise, if x * (x + 1) is less than or equal to n, answr is calculated based on a different formula.
    #State of the program after the if-else block has been executed: *N is an integer such that 1 ≤ N ≤ 10^6, n is an input integer; x is the square root of n. If x^2 = n, then answr is assigned the value of x * 4. Otherwise, if x * (x + 1) > n, answr is calculated based on certain conditions. If x * (x + 1) is less than or equal to n, answr is calculated based on a different formula.
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function `func` takes an input integer `n`, calculates the square root of `n`, and based on certain conditions involving the square of the square root, calculates a value for `answr`. The final value of `answr` is then converted to an integer and printed. The function does not accept any external parameters and does not return any value.

