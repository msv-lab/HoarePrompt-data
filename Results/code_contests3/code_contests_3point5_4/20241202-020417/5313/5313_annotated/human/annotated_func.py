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
        #State of the program after the if-else block has been executed: *N is an integer such that 1 <= N <= 10^6; n is assigned the value of N, x is the square root of n, the square of x is not equal to n. If x * (x + 1) > n, `answr` is the result of `(x + x + 1) * 2`. Otherwise, if x * (x + 1) is less than or equal to n, `answr` is 4 * (x + 1).
    #State of the program after the if-else block has been executed: *N is an integer such that 1 <= N <= 10^6, x is the square root of N, n is equal to N. If x
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function `func` reads an integer `N` from the user input, calculates a value based on the square root of `N`, and then determines `answr` based on certain conditions. The final `answr` is printed as an integer. The function does not accept any parameters and does not return any value.

