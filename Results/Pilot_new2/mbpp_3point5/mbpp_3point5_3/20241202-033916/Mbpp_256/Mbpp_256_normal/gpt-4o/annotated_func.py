#State of the program right berfore the function call: n is a non-negative integer.**
def func_1(n):
    if (n <= 2) :
        return 0
        #The program returns 0 if the value of n is less than or equal to 2, or when n is a non-negative integer.
    #State of the program after the if block has been executed: *n is a non-negative integer. n is larger than 2
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer larger than 2, `is_prime` is a list of length `n` filled with `True` values except for `is_prime[0] = False` and `is_prime[1] = False`. After the loop finishes executing, `is_prime` will have updated values where all multiples of prime numbers up to the square root of `n` have been marked as `False`, effectively marking non-prime numbers.
    return sum(is_prime)
    #The program returns the sum of `is_prime` after updating values where all multiples of prime numbers up to the square root of `n` have been marked as `False`
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n`. If `n` is less than or equal to 2, the function returns 0. For `n` greater than 2, the function updates values in a list `is_prime` where multiples of prime numbers up to the square root of `n` are marked as `False`, and then returns the sum of the `is_prime` values.

