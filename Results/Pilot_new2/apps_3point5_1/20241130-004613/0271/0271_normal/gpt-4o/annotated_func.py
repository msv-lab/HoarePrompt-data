#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^9.**
def func():
    n = int(input())
    remainder = n % 10
    if (remainder <= 5) :
        result = n - remainder
    else :
        result = n + (10 - remainder)
    #State of the program after the if-else block has been executed: *`n` is a non-negative integer such that 0 ≤ n ≤ 10^9, remainder is the remainder of n divided by 10. If remainder is less than or equal to 5, then the current value of remainder is less than or equal to 5. In this case, result is equal to the difference between n and remainder. If remainder is larger than 5, then result is equal to n + (10 - remainder).
    print(result)
#Overall this is what the function does:The function `func` takes user input as a non-negative integer `n` within the range of 0 to 10^9. It calculates the remainder of `n` divided by 10 and based on the value of the remainder, it adjusts the result accordingly. If the remainder is less than or equal to 5, the result is computed as the difference between `n` and the remainder. If the remainder is greater than 5, the result is calculated as `n` plus the difference between 10 and the remainder. The function then prints the result.

