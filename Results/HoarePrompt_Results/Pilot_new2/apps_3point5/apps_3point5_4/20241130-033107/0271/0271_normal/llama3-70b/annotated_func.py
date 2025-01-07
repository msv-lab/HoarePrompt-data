#State of the program right berfore the function call: n is a non-negative integer such that 0 <= n <= 10^9.**
def func():
    n = int(input())
    if (n % 10 == 0) :
        print(n)
    else :
        if (n % 10 <= 5) :
            print(n - n % 10)
        else :
            print(n + (10 - n % 10))
        #State of the program after the if-else block has been executed: *n is an input integer obtained from user input. n is not divisible by 10. If n % 10 <= 5, then the current value of n satisfies the condition. The expression n - n % 10 is printed. If n % 10 is larger than 5, the value printed is n + (10 - n % 10).
    #State of the program after the if-else block has been executed: *n is an input integer obtained from user input. If n is divisible by 10, the value of n is printed. Otherwise, if n is not divisible by 10, and n % 10 <= 5, then n - n % 10 is printed. If n % 10 > 5, then n + (10 - n % 10) is printed.
#Overall this is what the function does:The function `func` reads an integer `n` from user input and performs the following operations:
- If `n` is divisible by 10, it prints the value of `n`.
- If `n` is not divisible by 10, it checks if the remainder of `n` divided by 10 is less than or equal to 5. If true, it prints `n - n % 10`. If false, it prints `n + (10 - n % 10)`.
The function does not accept any parameters and does not return any value.

