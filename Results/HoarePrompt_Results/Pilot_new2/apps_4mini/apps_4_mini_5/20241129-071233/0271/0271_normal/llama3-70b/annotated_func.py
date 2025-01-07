#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^9.
def func():
    n = int(input())
    if (n % 10 == 0) :
        print(n)
    else :
        if (n % 10 <= 5) :
            print(n - n % 10)
        else :
            print(n + (10 - n % 10))
        #State of the program after the if-else block has been executed: *`n` is a non-negative integer such that 0 ≤ `n` ≤ 10^9 and is not a multiple of 10. If the remainder of `n` when divided by 10 is less than or equal to 5, the function returns the largest multiple of 10 less than or equal to `n`, which is `n - n % 10`. Otherwise, if the remainder is greater than 5, the function returns `n + (10 - n % 10)`, which rounds `n` up to the next multiple of 10.
    #State of the program after the if-else block has been executed: *`n` is a non-negative integer within the range 0 ≤ `n` ≤ 10^9. If `n` is divisible by 10, the function returns `n`. If `n` is not a multiple of 10 and the remainder of `n` when divided by 10 is less than or equal to 5, the function returns the largest multiple of 10 less than or equal to `n`, which is `n - n % 10`. Otherwise, if the remainder is greater than 5, the function returns `n + (10 - n % 10)`, rounding `n` up to the next multiple of 10.
#Overall this is what the function does:The function accepts a non-negative integer `n` from user input and prints the nearest multiple of 10 to `n`. If `n` is already a multiple of 10, it prints `n`. If `n` is not a multiple of 10 and the last digit is 5 or less, it prints the largest multiple of 10 less than or equal to `n`. If the last digit is greater than 5, it prints the smallest multiple of 10 greater than `n`. However, the function does not return any value; it only prints the result.

