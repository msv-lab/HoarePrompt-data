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
        #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^9 and `n` is larger than 2. If `n` is odd, the output values are `((n * n - 1) / 2, (n * n + 1) / 2)`. If `n` is even, the output values are `(n * n / 4 - 1, n * n / 4 + 1)`.
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^9. If `n` is less than or equal to 2, a SyntaxError occurs due to invalid syntax in the print statement. If `n` is greater than 2 and odd, the output values are `((n * n - 1) / 2, (n * n + 1) / 2)`. If `n` is greater than 2 and even, the output values are `(n * n / 4 - 1, n * n / 4 + 1)`.
#Overall this is what the function does:The function accepts a positive integer `n` inputted by the user, and if `n` is less than or equal to 2, it prints `-1`. If `n` is greater than 2 and odd, it prints two values: `((n * n - 1) / 2, (n * n + 1) / 2)`. If `n` is greater than 2 and even, it prints two values: `(n * n / 4 - 1, n * n / 4 + 1)`. The function does not return any values; it only prints the results based on the conditions. Note that there is a potential syntax error in the print statement for `n <= 2`, as it lacks parentheses in Python 3. Additionally, the function does not handle input validation or exceptions, which could lead to unexpected behavior if the input is not a valid integer.

