#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^9.**
def func():
    n = int(input())
    remainder = n % 10
    if (remainder <= 5) :
        result = n - remainder
    else :
        result = n + (10 - remainder)
    #State of the program after the if-else block has been executed: *n is a non-negative integer such that 0 ≤ n ≤ 10^9 and n is assigned the integer value entered by the user; remainder is the value of n modulo 10. If the current value of remainder is less than or equal to 5, then the result is equal to n - remainder. If the value of remainder is greater than 5, then the result is equal to n + (10 - remainder)
    print(result)
#Overall this is what the function does:This function `func` takes user input as a non-negative integer `n` with the constraint 0 ≤ n ≤ 10^9. It calculates the remainder of `n` divided by 10 and based on this remainder, it computes a result. If the remainder is less than or equal to 5, the result is n minus the remainder; otherwise, the result is n plus the difference between 10 and the remainder. The function then prints the calculated result.

