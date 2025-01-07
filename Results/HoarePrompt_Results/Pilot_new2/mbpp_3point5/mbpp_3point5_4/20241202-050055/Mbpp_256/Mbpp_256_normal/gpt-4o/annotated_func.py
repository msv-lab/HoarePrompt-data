#State of the program right berfore the function call: n is a non-negative integer.**
def func_1(n):
    if (n <= 2) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: *n is a non-negative integer. n is larger than 2.
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer larger than 2, `is_prime` is a list of boolean values where `is_prime[0] = is_prime[1] = False` and all other elements are True, all composite numbers up to `n` have been marked as False in `is_prime`, all prime numbers up to `n` have been marked as True in `is_prime`.
    return sum(is_prime)
    #The program returns the sum of boolean values in the list `is_prime`, where `is_prime[0] = is_prime[1] = False` and all other elements are True.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n`. If `n` is less than or equal to 2, the function returns 0. For `n` greater than 2, the function generates a list `is_prime` where elements represent whether the index is a prime number or not. It marks composite numbers as False and prime numbers as True. The function then returns the sum of boolean values in the list `is_prime`, excluding the first two elements.

