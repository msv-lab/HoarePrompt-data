#State of the program right berfore the function call: n is a positive integer such that 2 <= n <= 10^9.
def func_1(n):
    if (n <= 2) :
        return 'NO'
        #The program returns 'NO' because the current value of n is less than or equal to 2
    #State of the program after the if block has been executed: *`n` is a positive integer such that 2 <= `n` <= 10^9, and `n` is greater than 2.
    divisors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        
    #State of the program after the  for loop has been executed: `divisors` contains all unique divisors of `n` excluding 1 and `n`, `i` is the last integer checked (up to `int(math.sqrt(n))`), `n` is a positive integer such that 2 <= `n` <= 10^9 and `n` is greater than 2.
    if (not divisors) :
        return 'NO'
        #The program returns 'NO' indicating that there are no unique divisors of `n` excluding 1 and `n`, and that the current value of `divisors` is empty.
    #State of the program after the if block has been executed: *`divisors` contains all unique divisors of `n` excluding 1 and `n`, `i` is the last integer checked (up to `int(math.sqrt(n))`), `n` is a positive integer such that 2 <= `n` <= 10^9 and `n` is greater than 2, and `divisors` is not empty.
    k = len(divisors)
    fractions = [(1, d) for d in divisors]
    return f'YES\n{k}\n' + '\n'.join(f'{a} {b}' for a, b in fractions)
    #The program returns 'YES', the count of unique divisors excluding 1 and n (which is k), and a list of tuples (1, d) for each d in the unique divisors.
#Overall this is what the function does:The function accepts a positive integer `n`, returns 'NO' if `n` is less than or equal to 2, returns 'NO' if `n` has no unique divisors other than 1 and `n`, and returns 'YES' along with the count and list of unique divisors otherwise. It does not explicitly handle cases where `n` is prime or edge cases like `n = 4` with only one divisor.

