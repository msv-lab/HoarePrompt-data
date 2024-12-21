#State of the program right berfore the function call: n is a positive integer such that 2 <= n <= 10^9.
def func_1(n):
    if (n <= 2) :
        return 'NO'
        #The program returns 'NO' because the current value of n is less than or equal to 2, and n is a positive integer within the specified range.
    #State of the program after the if block has been executed: *n is a positive integer such that 2 <= n <= 10^9, and n is greater than 2.
    divisors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        
    #State of the program after the  for loop has been executed: `divisors` contains all divisors of `n` (excluding `n` itself), `n` is a positive integer such that 2 <= `n` <= 10^9 and `n` is greater than 2. If `n` is prime, `divisors` will be empty.
    if (not divisors) :
        return 'NO'
        #The program returns 'NO' indicating that n is a prime number, as the current value of divisors is empty, meaning there are no divisors of n excluding n itself.
    #State of the program after the if block has been executed: *`divisors` contains all divisors of `n` (excluding `n` itself), `n` is a positive integer such that 2 <= `n` <= 10^9 and `n` is greater than 2. Additionally, `divisors` is not empty, indicating that `n` is not prime.
    k = len(divisors)
    fractions = [(1, d) for d in divisors]
    return f'YES\n{k}\n' + '\n'.join(f'{a} {b}' for a, b in fractions)
    #The program returns 'YES' followed by the number of divisors `k`, where `k` is the number of elements in the list `divisors`, and then a list of fractions as tuples (1, d) for each divisor d in `divisors`.
#Overall this is what the function does:The function accepts a positive integer `n` (where 2 <= n <= 10^9). It returns 'NO' if `n` is less than or equal to 2 or if `n` is a prime number (indicated by no divisors being found excluding `n` itself). If `n` has divisors, the function returns 'YES', followed by the count of those divisors `k`, and a list of fractions represented as tuples `(1, d)` for each divisor `d`. The function correctly handles edge cases where `n` is exactly 2 or 3 (both return 'NO') and efficiently evaluates divisibility for larger values of `n` up to the specified upper bound.

