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
        #State of the program after the if-else block has been executed: *n is a positive integer greater than 2. If n is odd, then the function is executed with n being a positive odd integer greater than 2. If n is even, then the function is executed with n being a positive integer greater than 2 and the number n is even.
    #State of the program after the if-else block has been executed: *n is a positive integer. If n <= 2, then n is a positive integer such that 1 ≤ n ≤ 2. If n is odd and greater than 2, the function is executed with n being a positive odd integer greater than 2. If n is even and greater than 2, the function is executed with n being a positive integer greater than 2, and the number n is even.
#Overall this is what the function does:The function `func` reads a positive integer `n` from the user input. If `n` is less than or equal to 2, it prints -1. If `n` is greater than 2 and odd, it calculates and prints two values: (n^2 - 1) / 2 and (n^2 + 1) / 2. If `n` is greater than 2 and even, it calculates and prints two values: n^2 / 4 - 1 and n^2 / 4 + 1. The function does not return any value.

