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
        #State of the program after the if-else block has been executed: *N is an integer such that 1 ≤ N ≤ 10^6, x is the integer square root of n, and x^2 is not equal to n. If x * (x + 1) > n, the answer is (x + x + 1) * 2. Otherwise, if x * (x + 1) is less than or equal to n, the answer is 4 * (x + 1)
    #State of the program after the if-else block has been executed: *N is an integer such that 1 ≤ N ≤ 10^6, x is the integer square root of n. If x^2 is equal to n, the function returns 4 times the square root of n. Otherwise, if x * (x + 1) > n, the answer is (x + x + 1) * 2. If x * (x + 1) is less than or equal to n, the answer is 4 * (x + 1)
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function `func` reads an integer `n` from the user input, calculates the square root of `n`, and based on certain conditions, it determines a value for the variable `answr`. If the square of the calculated square root is equal to `n`, it assigns `4 * x` to `answr`. If `x * (x + 1) > n`, it assigns `(x + x + 1) * 2` to `answr`. If `x * (x + 1) <= n`, it assigns `4 * (x + 1)` to `answr`. Finally, it prints the integer value of `answr`. The function does not accept any parameters and does not explicitly return any value.

