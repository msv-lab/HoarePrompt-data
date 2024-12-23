#State of the program right berfore the function call: n is a positive integer such that 2 <= n <= 10^9.
def func_1(n):
    if (n <= 2) :
        return 'NO'
        #The program returns 'NO'
    #State of the program after the if block has been executed: n is a positive integer such that 2 < n <= 10^9
    divisors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that \(2 < n \leq 10^9\), `divisors` is a list containing all divisors of `n` that are greater than 1 and less than or equal to the square root of `n`, and `i` is the last divisor found (or `int(math.sqrt(n)) + 1` if no divisors were found).
    if (not divisors) :
        return 'NO'
        #The program returns 'NO'
    #State of the program after the if block has been executed: `n` is a positive integer such that \(2 < n \leq 10^9\), `divisors` is a list containing all divisors of `n` that are greater than 1 and less than or equal to the square root of `n`, and `i` is the last divisor found (or `int(math.sqrt(n)) + 1` if no divisors were found). The list `divisors` is not empty
    k = len(divisors)
    fractions = [(1, d) for d in divisors]
    return f'YES\n{k}\n' + '\n'.join(f'{a} {b}' for a, b in fractions)
    #`YES\nk\n` followed by each tuple (a, b) from the list `fractions` in the format 'a b', where `k` is the length of the list `divisors` and `fractions` is a list of tuples (1, d) for each divisor `d` in `divisors`
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` such that \(2 \leq n \leq 10^9\). It checks if `n` has any divisors other than 1 and itself within the range \(2 \leq d \leq \sqrt{n}\). If `n` has no such divisors, it returns 'NO'. Otherwise, it returns 'YES' followed by the number of divisors (`k`) and each divisor `d` paired with 1, formatted as '1 d'.

