#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^9.**
def func():
    n = int(raw_input())
    if (n <= 2) :
        print - 1
    else :
        if (n & 1) :
            print(n * n - 1) / 2, (n * n + 1) / 2
        else :
            print(n * n / 4 - 1), n * n / 4 + 1
        #State of the program after the if-else block has been executed: *`n` is a positive odd integer such that 1 ≤ n ≤ 10^9, and n is greater than 2. If n is odd, the two values printed are whole numbers. If n is odd, the first expression is (n^2 / 4) - 1, and the second expression is (n^2 / 4) + 1.
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ n ≤ 10^9. If n is less than or equal to 2, the program prints -1. If n is a positive odd integer greater than 2, two whole numbers are printed. If n is odd, the first printed value is (n^2 / 4) - 1, and the second printed value is (n^2 / 4) + 1.
#Overall this is what the function does:The function `func` reads an integer `n` from the user and based on the value of `n`, it either prints -1 if `n` is less than or equal to 2, or it calculates and prints specific values depending on whether `n` is odd or even. If `n` is odd and greater than 2, it prints two whole numbers derived from mathematical expressions. If `n` is even and greater than 2, it prints two values calculated based on other mathematical expressions. The function does not accept any input parameters and does not return any value.

