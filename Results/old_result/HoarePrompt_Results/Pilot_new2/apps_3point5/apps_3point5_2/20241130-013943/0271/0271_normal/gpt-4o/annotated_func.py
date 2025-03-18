#State of the program right berfore the function call: n is a non-negative integer.**
def func():
    n = int(input())
    remainder = n % 10
    if (remainder <= 5) :
        result = n - remainder
    else :
        result = n + (10 - remainder)
    #State of the program after the if-else block has been executed: *n is a non-negative integer, remainder is the remainder of n divided by 10. If remainder is less than or equal to 5, result is equal to n - remainder. If remainder is larger than 5, result is equal to n + (10 - remainder).
    print(result)
#Overall this is what the function does:The function `func` reads an input integer `n`, calculates the remainder of `n` divided by 10, and then based on the value of the remainder, adjusts `n` to a number that is either lower than or equal to `n` if the remainder is less than or equal to 5, or higher than `n` if the remainder is greater than 5. The function then prints the resulting value. The function does not explicitly return any value. However, it operates under the assumption that `n` is a non-negative integer.

