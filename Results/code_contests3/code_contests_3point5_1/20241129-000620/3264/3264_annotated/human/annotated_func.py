#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 10^9.**
def func():
    n = int(raw_input())
    if (n <= 2) :
        print - 1
    else :
        if (n & 1) :
            print(n * n - 1) / 2, (n * n + 1) / 2
        else :
            print(n * n / 4 - 1), n * n / 4 + 1
        #State of the program after the if-else block has been executed: *`n` is a positive odd integer such that 1 <= n <= 10^9 and the value of `n` is greater than 2. If `n` is an odd number, the two calculated values are ((n^2) - 1) / 2 and ((n^2) + 1) / 2. Otherwise, if `n` is an odd number, the output of the print statement is calculated as (n * n / 4 - 1) and (n * n / 4 + 1)
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 <= n <= 10^9. If n <= 2, then the function does nothing. Otherwise, if `n` is an odd number, the function calculates ((n^2) - 1) / 2 and ((n^2) + 1) / 2. If `n` is an even number, the function outputs (n * n / 4 - 1) and (n * n / 4 + 1).
#Overall this is what the function does:The function `func` reads an integer `n` from the user input and based on the value of `n`, it performs calculations and prints certain values. If `n` is less than or equal to 2, it prints -1. If `n` is a positive odd integer greater than 2, it calculates and prints ((n^2) - 1) / 2 and ((n^2) + 1) / 2. If `n` is a positive even integer greater than 2, it calculates and prints (n * n / 4 - 1) and (n * n / 4 + 1). The function does not have a return value.

