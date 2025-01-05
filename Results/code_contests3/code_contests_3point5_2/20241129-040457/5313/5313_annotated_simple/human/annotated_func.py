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
        #State of the program after the if-else block has been executed: *`x` is the integer square root of `n`. If `x * (x + 1) > n`, then `answr` is calculated based on the value of `x`. Otherwise, if `x * (x + 1) <= n`, then `answr` is `4 * (x + 1)`.
    #State of the program after the if-else block has been executed: *`x` is the integer square root of `n`. If `x
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function reads an integer `n` from the user, calculates the integer square root `x` of `n`, and based on certain conditions, determines the value of `answr`. If `x

