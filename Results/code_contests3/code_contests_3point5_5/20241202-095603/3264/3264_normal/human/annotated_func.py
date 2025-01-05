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
        #State of the program after the if-else block has been executed: *`n` is a positive integer between 3 and 10^9. If `n` is odd, then two new values are calculated: (n * n - 1) / 2 and (n * n + 1) / 2. If `n` is even, then two values are printed: n^2 / 4 - 1 and n^2 / 4 + 1.
    #State of the program after the if-else block has been executed: *`n` is a positive integer. If `n` is less than or equal to 2, the value of `n` remains the same. If `n` is a positive odd integer between 3 and 10^9, then two new values are calculated: ((n * n) - 1) / 2 and ((n * n) + 1) / 2. If `n` is a positive even integer between 3 and 10^9, then two new values are printed: (n^2 / 4) - 1 and (n^2 / 4) + 1.
#Overall this is what the function does:The function `func` reads an integer `n` from the user input and based on the value of `n`, it performs different calculations. If `n` is less than or equal to 2, it prints -1. If `n` is odd, it calculates and prints two values: ((n * n) - 1) / 2 and ((n * n) + 1) / 2. If `n` is even, it calculates and prints two values: (n^2 / 4) - 1 and (n^2 / 4) + 1. The function does not accept any parameters and does not return any values.

