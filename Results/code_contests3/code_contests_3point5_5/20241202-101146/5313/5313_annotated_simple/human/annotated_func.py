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
        #State of the program after the if-else block has been executed: *N is an integer such that 1 <= N <= 10^6, n is an input integer, x is the square root of n and x is not the square root of n. If x * (x + 1) > n, `answr` is calculated based on the given conditions. Otherwise, `answr` is the result of 4 * (x + 1)
    #State of the program after the if-else block has been executed: *N is an integer such that 1 <= N <= 10^6, n is an input integer, x is the square root of n. If x
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function reads an integer input `n`, calculates the square root of `n`, and based on certain conditions, computes and prints an integer `answr`. The function ensures that the final `answr` value is an integer. The functionality of the function is to calculate `answr` based on the square root of `n` and specific conditions, and print the result.

