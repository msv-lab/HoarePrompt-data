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
        #State of the program after the if-else block has been executed: *`n` is a non-negative integer such that 0 ≤ `n` ≤ 10^9 and `n` is not divisible by 10. If `n % 10` is less than or equal to 5, the output is the largest multiple of 10 less than `n`, which is `n - n % 10`. Otherwise, if `n % 10` is greater than 5, the output printed is 10.
    #State of the program after the if-else block has been executed: *`n` is a non-negative integer such that 0 ≤ `n` ≤ 10^9. If `n` is a multiple of 10, it is printed as is. If `n` is not divisible by 10 and `n % 10` is less than or equal to 5, the output is the largest multiple of 10 less than `n`, which is `n - n % 10`. If `n % 10` is greater than 5, the output printed is 10.
#Overall this is what the function does:The function accepts a non-negative integer `n` from user input and prints the nearest multiple of 10. If `n` is a multiple of 10, it prints `n`. If `n` is not divisible by 10 and `n % 10` is less than or equal to 5, it prints the largest multiple of 10 less than `n`. If `n % 10` is greater than 5, it prints the smallest multiple of 10 greater than `n`. The function does not return any value.

