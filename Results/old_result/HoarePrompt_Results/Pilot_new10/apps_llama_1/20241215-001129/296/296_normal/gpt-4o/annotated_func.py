#State of the program right berfore the function call: n is a positive integer such that 2 <= n <= 10^9.
def func_1(n):
    if (n <= 2) :
        return 'NO'
        #The program returns 'NO'
    #State of the program after the if block has been executed: n is a positive integer such that 2 <= n <= 10^9, and n is larger than 2
    divisors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 2 <= `n` <= 10^9, `i` is the largest integer less than or equal to the square root of `n`, `divisors` is a list containing all the divisors of `n` that are less than or equal to the square root of `n`.
    if (not divisors) :
        return 'NO'
        #The program returns 'NO'
    #State of the program after the if block has been executed: `n` is a positive integer such that 2 <= `n` <= 10^9, `i` is the largest integer less than or equal to the square root of `n`, `divisors` is a list containing all the divisors of `n` that are less than or equal to the square root of `n`, and `divisors` is not empty
    k = len(divisors)
    fractions = [(1, d) for d in divisors]
    return f'YES\n{k}\n' + '\n'.join(f'{a} {b}' for a, b in fractions)
    #The program returns a string that starts with 'YES', followed by the number of divisors of `n` that are less than or equal to the square root of `n`, and then lists each of these divisors in the format '1 d', where d is a divisor of `n` and is less than or equal to the square root of `n`.
#Overall this is what the function does:The function accepts a positive integer n between 2 and 10^9 and returns either 'NO' if n is less than or equal to 2 or if n is a prime number, or a string that starts with 'YES', followed by the number of divisors of n that are less than or equal to the square root of n, and then lists each of these divisors in the format '1 d', where d is a divisor of n and is less than or equal to the square root of n, but may include duplicate divisors if n is a perfect square.

