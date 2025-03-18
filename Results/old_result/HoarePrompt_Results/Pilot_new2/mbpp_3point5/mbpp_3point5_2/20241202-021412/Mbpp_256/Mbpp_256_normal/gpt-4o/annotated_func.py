#State of the program right berfore the function call: n is a non-negative integer.**
def func_1(n):
    if (n <= 2) :
        return 0
        #The program returns 0 when the value of n is less than or equal to 2
    #State of the program after the if block has been executed: *n is a non-negative integer. n is larger than 2.
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
        
    #State of the program after the  for loop has been executed: After the loop finishes executing, all elements of `is_prime` will be updated based on the Sieve of Eratosthenes algorithm. If `is_prime[i]` is True, then `is_prime[j]` where j is a multiple of i and in the range `[i * i, n)` will be set to False. All other `is_prime[j]` where j is not a multiple of i in the range `[i, n)` will remain True.
    return sum(is_prime)
    #The program returns the sum of all elements in the `is_prime` list after the Sieve of Eratosthenes algorithm has been applied.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n`. If `n` is less than or equal to 2, the function returns 0. If `n` is greater than 2, the function applies the Sieve of Eratosthenes algorithm to generate a list of prime numbers up to `n`, and then returns the sum of all prime numbers in the list. The function correctly implements the Sieve of Eratosthenes algorithm to determine prime numbers and calculates the sum accurately.

