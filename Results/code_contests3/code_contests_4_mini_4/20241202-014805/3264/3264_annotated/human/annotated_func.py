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
        #State of the program after the if-else block has been executed: *`n` is a positive integer greater than 2. If `n` is an odd integer, the outputs are `(n * n - 1) / 2` and `(n * n + 1) / 2`. If `n` is an even integer, the output values are `n * n / 4 - 1` and `n * n / 4 + 1`.
    #State of the program after the if-else block has been executed: *`n` is a positive integer based on user input. If `n` is less than or equal to 2, a syntax error occurs due to an invalid print statement. If `n` is greater than 2 and odd, the outputs are `(n * n - 1) / 2` and `(n * n + 1) / 2`. If `n` is greater than 2 and even, the output values are `n * n / 4 - 1` and `n * n / 4 + 1`.
#Overall this is what the function does:The function accepts a positive integer input `n` from the user. If `n` is less than or equal to 2, it prints -1. If `n` is greater than 2 and odd, it calculates and prints two values: `(n * n - 1) / 2` and `(n * n + 1) / 2`. If `n` is greater than 2 and even, it calculates and prints two different values: `n * n / 4 - 1` and `n * n / 4 + 1`. There is no explicit return value from the function, as it only prints output to the console.

