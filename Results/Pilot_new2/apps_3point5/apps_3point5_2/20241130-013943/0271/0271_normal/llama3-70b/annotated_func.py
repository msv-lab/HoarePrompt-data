#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^9.**
def func():
    n = int(input())
    if (n % 10 == 0) :
        print(n)
    else :
        if (n % 10 <= 5) :
            print(n - n % 10)
        else :
            print(n + (10 - n % 10))
        #State of the program after the if-else block has been executed: *n is a non-negative integer such that 0 ≤ n ≤ 10^9 and n is not divisible by 10. If n % 10 is less than or equal to 5, then n - n % 10 is calculated and printed. If n % 10 is larger than 5, the remainder of n divided by 10 is larger than 5.
    #State of the program after the if-else block has been executed: *n is a non-negative integer such that 0 ≤ n ≤ 10^9. If n is divisible by 10, then the current value of n remains unchanged. If n is not divisible by 10, then depending on the value of n % 10, if it is less than or equal to 5, n is updated to n - n % 10. If n % 10 is greater than 5, the remainder of n divided by 10 is greater than 5.
#Overall this is what the function does:The function `func` reads an integer `n` from the user and then based on the value of `n`, it performs specific calculations and prints a modified version of `n`. If `n` is divisible by 10, it prints `n`. If `n` is not divisible by 10, it rounds `n` down to the nearest multiple of 10. The function does not accept any parameters and returns nothing.

