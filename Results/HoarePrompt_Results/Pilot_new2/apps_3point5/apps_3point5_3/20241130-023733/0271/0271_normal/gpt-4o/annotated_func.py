#State of the program right berfore the function call: n is a non-negative integer (0 ≤ n ≤ 10^9).
def func():
    n = int(input())
    remainder = n % 10
    if (remainder <= 5) :
        result = n - remainder
    else :
        result = n + (10 - remainder)
    #State of the program after the if-else block has been executed: *n is a non-negative integer (0 ≤ n ≤ 10^9), remainder is the remainder of n divided by 10. If remainder is less than or equal to 5, then result is equal to n - remainder. If remainder is greater than 5, then result is equal to n + (10 - remainder).
    print(result)
#Overall this is what the function does:The function `func` reads an integer input `n`, calculates the remainder of `n` divided by 10, and based on the value of the remainder, adjusts `n` to be either rounded down to the nearest multiple of 10 or rounded up. The adjusted value is then printed as the result. The function does not accept any parameters and returns nothing. Potential edge cases or missing functionality include handling negative inputs, as the current annotation only specifies non-negative integers and not covering the case where the remainder is exactly 5.

