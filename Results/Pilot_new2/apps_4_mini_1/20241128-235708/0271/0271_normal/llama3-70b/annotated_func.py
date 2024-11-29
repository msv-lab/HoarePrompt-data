#State of the program right berfore the function call: n is a non-negative integer such that 0 <= n <= 10^9.
def func():
    n = int(input())
    if (n % 10 == 0) :
        print(n)
    else :
        if (n % 10 <= 5) :
            print(n - n % 10)
        else :
            print(n + (10 - n % 10))
        #State of the program after the if-else block has been executed: *`n` is a non-negative integer such that 0 <= `n` <= 10^9 and not a multiple of 10. If `n % 10 <= 5`, the output is `n - n % 10`, which is a multiple of 10 less than `n`. Otherwise, the output is `n - n % 10 + 10`, which is a multiple of 10 greater than `n`.
    #State of the program after the if-else block has been executed: *`n` is a non-negative integer such that 0 <= `n` <= 10^9. If `n` is a multiple of 10, it is printed. If `n` is not a multiple of 10 and `n % 10 <= 5`, the output is the largest multiple of 10 less than `n`. Otherwise, the output is the smallest multiple of 10 greater than `n`.
#Overall this is what the function does:The function does not accept any parameters and prompts the user for a non-negative integer `n`. It prints `n` if it is a multiple of 10. If `n` is not a multiple of 10, it prints the largest multiple of 10 that is less than `n` if the last digit of `n` is 5 or less, or the smallest multiple of 10 that is greater than `n` if the last digit is greater than 5.

