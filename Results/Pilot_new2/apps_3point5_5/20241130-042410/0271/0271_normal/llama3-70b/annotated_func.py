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
        #State of the program after the if-else block has been executed: *`n` is a non-negative integer such that 0 ≤ n ≤ 10^9, where n % 10 is not equal to 0. If n % 10 is less than or equal to 5, then `n` is updated to n - n % 10. Otherwise, when n % 10 is larger than 5, `n` is updated to n + (10 - n % 10)
    #State of the program after the if-else block has been executed: *n is a non-negative integer such that 0 ≤ n ≤ 10^9. If n % 10 == 0, n is printed. If n % 10 is not equal to 0, then n is updated based on the following conditions: if n % 10 is less than or equal to 5, n is updated to n - n % 10. If n % 10 is larger than 5, n is updated to n + (10 - n % 10).
#Overall this is what the function does:The function prompts the user to input a non-negative integer `n` between 0 and 10^9. If n is divisible by 10, it prints n. If n is not divisible by 10, it adjusts n based on whether n % 10 is less than or equal to 5 or greater than 5, and then prints the adjusted value. The function does not accept any parameters and does not return any value.

