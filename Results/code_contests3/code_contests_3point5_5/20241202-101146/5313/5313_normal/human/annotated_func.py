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
        #State of the program after the if-else block has been executed: *N is an integer such that 1 <= N <= 10^6, `n` is an input integer, `x` is the integer square root of `n`, `answr` is calculated as (x + x + 1) * 2 if x * (x + 1) > n, otherwise `answr` is calculated as `4 * (x + 1)`.
    #State of the program after the if-else block has been executed: *N is an integer such that 1 <= N <= 10^6, `n` is an input integer, `x` is the integer square root of `n`, `answr` is calculated as 4 times the square root of `n` if x^2 == n. If x^2 != n, then `answr` is calculated as (x + x + 1) * 2 if x * (x + 1) > n, otherwise `answr` is calculated as `4 * (x + 1)`
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function `func` takes an integer input `n` from the user, calculates the square root of `n`, and based on certain conditions calculates the value of `answr`. If the square of the square root of `n` equals `n`, `answr` is set to 4 times the square root of `n`. If not, it checks if the product of the square root and its successor is greater than `n`, then sets `answr` to (x + x + 1) * 2, otherwise sets `answr` to `4 * (x + 1)`. Finally, it prints the integer value of `answr`. The function does not take any parameters and does not return a value.

