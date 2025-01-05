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
        #State of the program after the if-else block has been executed: *`N` is a positive integer such that 1 <= N <= 10^6; `n` is the input integer provided by the user; `x` is the square root of `n` as an integer. The square of `x` is not equal to `n`. If `x * (x + 1) > n`, then the function sets `answr` as the result of `(x + x + 1) * 2`. Otherwise, if `x * (x + 1) <= n`, the function calculates `answr` based on the given conditions.
    #State of the program after the if-else block has been executed: *N is a positive integer such that 1 <= N <= 10^6; n is the input integer provided by the user; x is the square root of n as an integer. If x^2 == n, then answr is 4 times the square root of n. If x^2 != n, the function checks if x * (x + 1) > n. If true, answr is set to (x + x + 1) * 2. If false, answr is calculated based on other conditions.
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function `func` reads an integer input `n` from the user, calculates the square root `x` of `n`, and then determines the value of `answr` based on specific conditions. If `x` squared equals `n`, `answr` is set to 4 times the square root of `n`. If not, it checks if `x * (x + 1) > n`, setting `answr` to `(x + x + 1) * 2` if true, and to `4 * (x + 1)` otherwise. The final value of `answr` is then printed. The function does not accept any parameters and does not return any value.

