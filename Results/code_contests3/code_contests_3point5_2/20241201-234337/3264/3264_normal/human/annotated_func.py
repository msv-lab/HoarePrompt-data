#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 109).**
def func():
    n = int(raw_input())
    if (n <= 2) :
        print - 1
    else :
        if (n & 1) :
            print(n * n - 1) / 2, (n * n + 1) / 2
        else :
            print(n * n / 4 - 1), n * n / 4 + 1
        #State of the program after the if-else block has been executed: *`n` is a positive integer larger than 2. If `n` is an odd number, two calculated integer values are obtained based on the expressions provided. If `n` is a positive odd integer (1 ≤ n ≤ 109), values of the expressions are calculated based on the formula provided.
    #State of the program after the if-else block has been executed: *`n` is a positive integer. If `n` is less than or equal to 2, there is no change in the state of the program variables. If `n` is a positive integer larger than 2, two calculated integer values are obtained based on the expressions provided. If `n` is a positive odd integer (1 ≤ n ≤ 109), values of the expressions are calculated based on the formula provided.
#Overall this is what the function does:The function `func` reads an integer `n` from input and performs calculations based on the value of `n`. If `n` is less than or equal to 2, it prints -1. If `n` is a positive odd integer, it calculates two integer values based on specific formulas and prints them. If `n` is a positive even integer, it calculates two integer values using different formulas and prints them. The function does not accept any parameters and returns nothing.

