#State of the program right berfore the function call: n is a positive integer such that 2 ≤ n ≤ 10^9.
def func_1(n):
    if (n <= 2) :
        return 'NO'
        #The program returns 'NO'
    #State of the program after the if block has been executed: n is a positive integer such that 2 ≤ n ≤ 10^9, and n is greater than 2
    divisors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that \(2 \leq n \leq 10^9\) and \(n > 2\); `divisors` is a list containing all unique divisors of `n` from 2 to \(\lfloor\sqrt{n}\rfloor\) along with their corresponding quotients, ensuring no duplicates.
    if (not divisors) :
        return 'NO'
        #The program returns 'NO'
    #State of the program after the if block has been executed: `n` is a positive integer such that \(2 \leq n \leq 10^9\) and \(n > 2\); `divisors` is a list containing all unique divisors of `n` from 2 to \(\lfloor\sqrt{n}\rfloor\) along with their corresponding quotients, ensuring no duplicates. The list `divisors` is not empty
    k = len(divisors)
    fractions = [(1, d) for d in divisors]
    return f'YES\n{k}\n' + '\n'.join(f'{a} {b}' for a, b in fractions)
    #The program returns a string starting with 'YES', followed by the length of the 'divisors' list (denoted as k), and then each tuple in the 'fractions' list formatted as '1 d' where 'd' is a divisor of 'n' from 2 to \(\lfloor\sqrt{n}\rfloor\), along with its corresponding quotient
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` such that \(2 \leq n \leq 10^9\). It first checks if `n` is less than or equal to 2, returning 'NO' if true. If `n` is greater than 2, it calculates all unique divisors of `n` from 2 to \(\lfloor\sqrt{n}\rfloor\) and their corresponding quotients, storing them in the `divisors` list. If the `divisors` list is empty, it returns 'NO'. Otherwise, it returns a string starting with 'YES', followed by the length of the `divisors` list, and then each tuple in the `fractions` list formatted as '1 d' where 'd' is a divisor of `n` from 2 to \(\lfloor\sqrt{n}\rfloor\), along with its corresponding quotient.

