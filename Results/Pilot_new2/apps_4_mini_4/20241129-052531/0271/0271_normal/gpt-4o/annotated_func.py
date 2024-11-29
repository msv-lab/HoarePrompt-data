#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^9.
def func():
    n = int(input())
    remainder = n % 10
    if (remainder <= 5) :
        result = n - remainder
    else :
        result = n + (10 - remainder)
    #State of the program after the if-else block has been executed: *`n` is an input integer such that 0 ≤ `n` ≤ 10^9. If `remainder` (which is `n % 10`) is between 0 and 5, then `result` is set to `n - remainder`. If `remainder` is between 6 and 9, then `result` is set to `n + (10 - remainder)`.
    print(result)
#Overall this is what the function does:The function accepts a non-negative integer `n` (input by the user) and rounds it to the nearest multiple of 10. If the last digit of `n` (i.e., `n % 10`) is 0 to 5, it subtracts the last digit from `n`. If the last digit is 6 to 9, it adds the difference to reach the next multiple of 10. The result is printed, but the function does not return any value.

