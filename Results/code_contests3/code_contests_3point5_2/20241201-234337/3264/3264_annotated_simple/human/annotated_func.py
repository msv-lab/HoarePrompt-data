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
        #State of the program after the if-else block has been executed: *`n` is a positive integer larger than 2 and an odd number. If `n` is odd, the function performs the first calculation. If `n` is odd, the result of the first calculation is an even number. If `n` is even, the result of the second calculation is an even number.
    #State of the program after the if-else block has been executed: *`n` is a positive integer. If `n` is less than or equal to 2, the function does nothing. If `n` is a positive integer larger than 2 and an odd number, the function performs the first calculation. The result of the first calculation is an even number if `n` is odd. If `n` is even, the result of the second calculation is an even number.
#Overall this is what the function does:The function `func` reads an integer `n` from the user and performs calculations based on the value of `n`. If `n` is less than or equal to 2, the function prints -1. If `n` is a positive integer larger than 2 and an odd number, the function calculates and prints two values: (n * n - 1) / 2 and (n * n + 1) / 2. If `n` is an even number, the function calculates and prints two values: n * n / 4 - 1 and n * n / 4 + 1.

