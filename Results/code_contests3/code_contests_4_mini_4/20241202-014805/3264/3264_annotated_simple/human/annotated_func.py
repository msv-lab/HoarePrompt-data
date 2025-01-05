#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^9.
def func():
    n = int(raw_input())
    if (n <= 2) :
        print - 1
    else :
        if (n & 1) :
            print(n * n - 1) / 2, (n * n + 1) / 2
        else :
            print(n * n / 4 - 1), n * n / 4 + 1
        #State of the program after the if-else block has been executed: *`n` is a positive integer greater than 2. If `n` is odd, the outputs are `(n * n - 1) / 2` and `(n * n + 1) / 2`. If `n` is even, the outputs are `(n * n / 4 - 1)` and `(n * n / 4 + 1)`.
    #State of the program after the if-else block has been executed: *`n` is a positive integer. If `n` is less than or equal to 2, there is a syntax error in the print statement. If `n` is greater than 2 and odd, the outputs are `(n * n - 1) / 2` and `(n * n + 1) / 2`. If `n` is greater than 2 and even, the outputs are `(n * n / 4 - 1)` and `(n * n / 4 + 1)`.
#Overall this is what the function does:The function accepts a positive integer `n` via user input (with the constraint 1 ≤ n ≤ 10^9). If `n` is less than or equal to 2, it prints `-1`. If `n` is greater than 2 and odd, it prints the values `(n * n - 1) / 2` and `(n * n + 1) / 2`. If `n` is greater than 2 and even, it prints `(n * n / 4 - 1)` and `(n * n / 4 + 1)`. The function does not return any value, and it relies on print statements for output instead.

