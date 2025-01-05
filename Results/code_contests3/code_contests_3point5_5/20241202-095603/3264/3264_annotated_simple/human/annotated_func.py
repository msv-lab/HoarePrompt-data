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
        #State of the program after the if-else block has been executed: *`n` is a positive integer between 3 and 10^9 inclusive. If `n` is an odd number, the function updates `n` to a positive odd integer between 3 and 10^9 inclusive. If `n` is an even number, the function keeps `n` as a positive integer between 3 and 10^9 inclusive.
    #State of the program after the if-else block has been executed: *`n` is a positive integer between 1 and 10^9. If `n` is less than or equal to 2, the function does not modify `n`. If `n` is between 3 and 10^9 inclusive, the function updates `n` to be a positive odd integer between 3 and 10^9 inclusive if `n` is odd. If `n` is an even number, the function keeps `n` as a positive integer between 3 and 10^9 inclusive.
#Overall this is what the function does:The function `func` reads an integer `n` from the user input. If `n` is less than or equal to 2, it prints -1. If `n` is greater than 2, it calculates and prints two values based on whether `n` is odd or even. For odd `n`, it prints two values derived from `n`. For even `n`, it calculates and prints two values. The function does not accept any parameters and does not return anything.

