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
        #State of the program after the if-else block has been executed: *`n` is a positive odd integer such that 1 ≤ n ≤ 10^9 and n is larger than 2. If n is an odd positive integer, where n * n - 1 is divisible by 2 and n * n + 1 is divisible by 2, then the program returns the values (n * n - 1) / 2 and (n * n + 1) / 2. If n is an odd positive integer, where 1 ≤ n ≤ 10^9, the program returns n * n / 4 - 1 and n * n / 4 + 1.
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ n ≤ 10^9. If n is less than or equal to 2, then the function does nothing. If n is a positive odd integer larger than 2, where n * n - 1 is divisible by 2 and n * n + 1 is divisible by 2, the function returns the values ((n * n - 1) / 2) and ((n * n + 1) / 2). If n is an odd positive integer between 1 and 10^9, the function returns (n * n / 4 - 1) and (n * n / 4 + 1).
#Overall this is what the function does:The function `func` reads an integer `n` from the user input. If `n` is less than or equal to 2, it prints -1. If `n` is a positive odd integer greater than 2, it prints the values ((n * n - 1) / 2) and ((n * n + 1) / 2). If `n` is an odd positive integer between 1 and 10^9, it prints (n * n / 4 - 1) and (n * n / 4 + 1). The function does not accept any parameters explicitly and does not have a return value.

