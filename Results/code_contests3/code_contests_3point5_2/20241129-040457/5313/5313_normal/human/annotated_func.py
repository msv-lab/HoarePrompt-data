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
        #State of the program after the if-else block has been executed: *N is an integer such that 1 ≤ N ≤ 10^6, n is an input integer, x is the square root of n which is not a perfect square root of n. If x * (x + 1) > n, answr is a decimal number. Otherwise, answr is 4 * (x + 1)
    #State of the program after the if-else block has been executed: *N is an integer such that 1 ≤ N ≤ 10^6, n is an input integer, x is the square root of n. If x^2 = n, answr is either 4 times the square root of n or -4 times the square root of n. If x * (x + 1) > n, answr is a decimal number. Otherwise, answr is 4 * (x + 1)
    answr = int(answr)
    print(answr)
#Overall this is what the function does:The function prompts the user for an integer input `n`, calculates the square root of `n`, and based on certain conditions, determines the value of `answr`. If the square of the square root of `n` equals `n`, `answr` is set to either 4 times or -4 times the square root of `n`. If `x * (x + 1)` is greater than `n`, `answr` is a decimal number; otherwise, it is set to 4 times the square root of `n` plus 4. The final result is printed as an integer. The function does not accept any parameters and does not explicitly return a value.

