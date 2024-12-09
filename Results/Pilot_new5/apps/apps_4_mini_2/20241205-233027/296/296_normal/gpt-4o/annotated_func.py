#State of the program right berfore the function call: n is a positive integer such that 2 <= n <= 10^9.
def func_1(n):
    if (n <= 2) :
        return 'NO'
        #The program returns 'NO' since the current value of 'n' is less than or equal to 2
    #State of the program after the if block has been executed: *n is a positive integer such that 2 <= n <= 10^9, and n is greater than 2.
    divisors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 2 <= `n` <= 10^9; `divisors` is a list containing all divisors of `n` (excluding `n` itself) that are less than or equal to `sqrt(n)`, including both `i` and `n // i` whenever applicable. If `n` is prime, then `divisors` will be an empty list.
    if (not divisors) :
        return 'NO'
        #The program returns 'NO' indicating that `n` is a prime number, as the list of divisors is empty.
    #State of the program after the if block has been executed: *`n` is a positive integer such that 2 <= `n` <= 10^9; `divisors` is a list containing all divisors of `n` (excluding `n` itself) that are less than or equal to `sqrt(n)`, including both `i` and `n // i` whenever applicable. `divisors` is not an empty list, meaning `n` is not a prime number.
    k = len(divisors)
    fractions = [(1, d) for d in divisors]
    return f'YES\n{k}\n' + '\n'.join(f'{a} {b}' for a, b in fractions)
    #The program returns 'YES', followed by the count of the divisors 'k', and then each fraction in 'fractions' which is a list of tuples (1, d) for each divisor 'd' in 'divisors'
#Overall this is what the function does:The function accepts a positive integer `n` (where `2 <= n <= 10^9`) and returns 'NO' if `n` is less than or equal to 2, or if `n` is a prime number (indicating that there are no divisors other than 1 and itself). If `n` is not prime, it returns 'YES', followed by the count of divisors of `n` (excluding `n` itself`), and a list of fractions in the form (1, d) for each divisor `d` found.

