#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^9.
def func():
    n = int(input())
    remainder = n % 10
    if (remainder <= 5) :
        result = n - remainder
    else :
        result = n + (10 - remainder)
    #State of the program after the if-else block has been executed: *`n` is an input integer such that 0 ≤ `n` ≤ 10^9; if `remainder` is less than or equal to 5, then `result` is equal to `n - remainder`. Otherwise, if `remainder` is greater than 5, then `result` is equal to `n + (10 - remainder)`.
    print(result)
#Overall this is what the function does:The function accepts no parameters, reads a non-negative integer from input, calculates the nearest multiple of 10 based on the last digit of that integer, and prints the result. It does not return any value.

