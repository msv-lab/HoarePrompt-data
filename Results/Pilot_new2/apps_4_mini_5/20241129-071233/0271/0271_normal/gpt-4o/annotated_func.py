#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^9.
def func():
    n = int(input())
    remainder = n % 10
    if (remainder <= 5) :
        result = n - remainder
    else :
        result = n + (10 - remainder)
    #State of the program after the if-else block has been executed: *`n` is a non-negative integer such that 0 ≤ `n` ≤ 10^9; if `remainder` (where `remainder` is equal to `n % 10`) is less than or equal to 5, then `result` is equal to `n - remainder`. Otherwise, if `remainder` is greater than 5, then `result` is equal to `n + (10 - remainder)`.
    print(result)
#Overall this is what the function does:The function prompts the user to input a non-negative integer `n` (where 0 ≤ n ≤ 10^9) and rounds it to the nearest multiple of 10. If the last digit of `n` (the remainder of `n` when divided by 10) is less than or equal to 5, the function subtracts the remainder from `n`. If the last digit is greater than 5, it adds the difference to reach the next multiple of 10. The result is printed; however, no value is returned from the function.

