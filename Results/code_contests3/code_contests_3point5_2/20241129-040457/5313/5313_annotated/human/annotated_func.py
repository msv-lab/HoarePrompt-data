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
        #State of the program after the if-else block has been executed: *N is an integer such that 1 ≤ N ≤ 10^6, n is an input integer, x is the integer square root of n. If the product of x and (x + 1) is greater than n, `answr` is assigned the value of `(x + x + 1) * 2`. Otherwise, if the condition (x * (x + 1) > n) is false, `answr` is equal to 4 times the integer square root of n plus 4.
    #State of the program after the if-else block has been executed: *N is an integer such that 1 ≤ N ≤ 10^6, n is an input integer, x is the integer square root of n. If the square of x equals n, `answr` is 4 times the integer square root of n. Otherwise, if the product of x and (x + 1) is greater than n, `answr` is assigned the value of `(x + x + 1) * 2`. If the condition (x * (x + 1) > n) is false, `answr` is equal to 4 times the integer square root of n plus 4.
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function `func` takes an integer input `n`, calculates the integer square root `x` of `n`, and based on certain conditions, determines the value of `answr`. If the square of `x` equals `n`, `answr` is set to 4 times `x`. If the product of `x` and (`x + 1`) is greater than `n`, `answr` is assigned `(x + x + 1) * 2`. Otherwise, `answr` is set to 4 times `x` plus 4. The final value of `answr` is then printed. The function does not have any return value.

