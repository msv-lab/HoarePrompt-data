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
        #State of the program after the if-else block has been executed: *`n` is an integer such that 0 ≤ `n` ≤ 10^9 and `n` is not a multiple of 10. If `n % 10` is less than or equal to 5, the result is `n - n % 10`, which is the largest multiple of 10 less than `n`. If `n % 10` is greater than 5, the result is `n + (10 - n % 10)`, which is the smallest multiple of 10 greater than `n`.
    #State of the program after the if-else block has been executed: *`n` is an integer such that 0 ≤ `n` ≤ 10^9. If `n` is a multiple of 10, `n` is printed. If `n` is not a multiple of 10 and `n % 10` is less than or equal to 5, the result is the largest multiple of 10 less than `n`. If `n % 10` is greater than 5, the result is the smallest multiple of 10 greater than `n`.
#Overall this is what the function does:The function accepts a non-negative integer `n` (where \(0 \leq n \leq 10^9\)) and prints the nearest multiple of 10 to `n`. If `n` is already a multiple of 10, it prints `n`. If `n` is not a multiple of 10, it prints the largest multiple of 10 less than `n` if the last digit is 5 or less, and the smallest multiple of 10 greater than `n` if the last digit is greater than 5. The function does not return any value.

