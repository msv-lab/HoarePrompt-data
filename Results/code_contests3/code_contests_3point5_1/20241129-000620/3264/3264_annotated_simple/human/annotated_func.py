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
        #State of the program after the if-else block has been executed: *n is a positive integer such that 1 ≤ n ≤ 10^9, n is larger than 2. If n is an odd integer, the result of the first expression is a perfect square number, and the result of the second expression is the next perfect square number. If n is an even integer, then the result of the first expression is a perfect square number, and the result of the second expression is the next perfect square number.
    #State of the program after the if-else block has been executed: *n is a positive integer such that 1 ≤ n ≤ 10^9. If n ≤ 2, the function does nothing. If n is larger than 2, then for odd n, the first expression results in a perfect square number, and the second expression results in the next perfect square number. For even n, the first expression results in a perfect square number, and the second expression results in the next perfect square number.
#Overall this is what the function does:The function `func` reads an integer `n` from the user input, where n is a positive integer in the range 1 ≤ n ≤ 10^9. If n is less than or equal to 2, the function prints -1. For n greater than 2, if n is odd, it prints a perfect square number followed by the next perfect square number. If n is even, it prints a perfect square number subtracted by 1 followed by the same perfect square number added by 1.

