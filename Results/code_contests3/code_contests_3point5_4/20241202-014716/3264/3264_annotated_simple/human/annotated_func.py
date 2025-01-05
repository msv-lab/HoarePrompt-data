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
        #State of the program after the if-else block has been executed: *`n` is a positive odd integer such that 1 ≤ n ≤ 10^9 and greater than 2. If `n` is an odd number, after execution, the program variables will be (n * n - 1) / 2 and (n * n + 1) / 2. If `n` is not an odd number, the variables will be (n * n / 4 - 1) and (n * n / 4 + 1).
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ n ≤ 10^9. If n ≤ 2, the function does not change the state of the variables. If n is a positive odd integer greater than 2, the program variables will be (n * n - 1) / 2 and (n * n + 1) / 2. If n is not an odd number, the variables will be (n * n / 4 - 1) and (n * n / 4 + 1).
#Overall this is what the function does:The function `func` reads an integer `n` from the user and performs calculations based on the value of `n`. If `n` is less than or equal to 2, it prints -1. If `n` is a positive odd integer greater than 2, it calculates and prints two values: (n * n - 1) / 2 and (n * n + 1) / 2. If `n` is not an odd number, it calculates and prints (n * n / 4 - 1) and (n * n / 4 + 1). The function does not have any return value.

