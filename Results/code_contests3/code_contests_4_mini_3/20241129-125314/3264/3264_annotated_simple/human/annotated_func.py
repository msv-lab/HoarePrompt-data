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
        #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^9 and `n` is greater than 2. If `n` is odd, the results are integers for both expressions. If `n` is even, the output of the print statement is (n * n / 4 - 1, n * n / 4 + 1).
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^9. If `n` is set to a value between 1 and 2, a syntax error occurs in the print statement. If `n` is greater than 2, and `n` is odd, the results are integers for both expressions. If `n` is even, the output of the print statement is (n * n / 4 - 1, n * n / 4 + 1).
#Overall this is what the function does:The function accepts a positive integer `n` obtained from user input and prints specific outputs based on the value of `n`. If `n` is less than or equal to 2, it prints `-1`. If `n` is odd (greater than 2), it prints two values calculated from `n`, specifically `(n * n - 1) / 2` and `(n * n + 1) / 2`. If `n` is even (greater than 2), it prints `(n * n / 4 - 1)` and `(n * n / 4 + 1)`. The function does not return any values, but prints results directly to the output. There is a missing handling for the case when `n` is 1 or 2, as it leads to a scenario that is not described in the annotations.

