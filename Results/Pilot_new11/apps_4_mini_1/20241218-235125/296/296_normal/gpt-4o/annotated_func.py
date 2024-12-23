#State of the program right berfore the function call: n is a positive integer such that 2 <= n <= 10^9.
def func_1(n):
    if (n <= 2) :
        return 'NO'
        #The program returns 'NO' because the current value of n is less than or equal to 2.
    #State of the program after the if block has been executed: *`n` is a positive integer such that 2 <= `n` <= 10^9, and `n` is greater than 2.
    divisors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        
    #State of the program after the  for loop has been executed: `divisors` contains all divisors of `n` except for `n` itself and is a list of integers greater than or equal to 2 that divides `n` without a remainder. If `n` is prime, then `divisors` remains an empty list.
    if (not divisors) :
        return 'NO'
        #The program returns 'NO' because the current value of `divisors` is empty, indicating that `n` is a prime number and has no divisors except for 1 and itself.
    #State of the program after the if block has been executed: *`divisors` contains all divisors of `n` except for `n` itself and is a non-empty list of integers greater than or equal to 2 that divides `n` without a remainder. This indicates that `n` is not prime.
    k = len(divisors)
    fractions = [(1, d) for d in divisors]
    return f'YES\n{k}\n' + '\n'.join(f'{a} {b}' for a, b in fractions)
    #The program returns 'YES', the number of divisors k, and each fraction formed by the tuples (1, d) for each d in the list of divisors
#Overall this is what the function does:The function accepts a positive integer `n` (where 2 <= n <= 10^9). It checks if `n` is less than or equal to 2, returning 'NO' in such cases. If `n` is a prime number (indicated by an empty list of divisors), it also returns 'NO'. If `n` is not prime, it collects all divisors of `n` (other than 1 and `n` itself), returning 'YES' along with the count of these divisors and a list of fractions of the form (1, d) for each divisor `d`. The function handles potential edge cases involving the smallest inputs and correctly identifies prime numbers.

