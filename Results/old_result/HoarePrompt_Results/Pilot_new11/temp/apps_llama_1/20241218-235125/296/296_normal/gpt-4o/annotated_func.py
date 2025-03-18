#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^9.
def func_1(n):
    if (n <= 2) :
        return 'NO'
        #The program returns 'NO'
    #State of the program after the if block has been executed: n is an integer such that 2 <= n <= 10^9, and n is strictly larger than 2
    divisors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= `n` <= 10^9 and `n` is strictly larger than 2, `i` is `int(math.sqrt(n))`, `divisors` is a list containing all divisors of `n` up to the square root of `n` and their corresponding quotients (if they are not equal to the divisor). If `n` is less than 2 or `int(math.sqrt(n))` is less than 2, `divisors` is an empty list.
    if (not divisors) :
        return 'NO'
        #The program returns 'NO'
    #State of the program after the if block has been executed: `n` is an integer such that 2 <= `n` <= 10^9 and `n` is strictly larger than 2, `i` is `int(math.sqrt(n))`, `divisors` is a list containing all divisors of `n` up to the square root of `n` and their corresponding quotients (if they are not equal to the divisor), and `divisors` is not empty, meaning that `n` is at least 2 and `int(math.sqrt(n))` is at least 2.
    k = len(divisors)
    fractions = [(1, d) for d in divisors]
    return f'YES\n{k}\n' + '\n'.join(f'{a} {b}' for a, b in fractions)
    #The program returns a string that starts with 'YES', followed by the number of divisors and their quotients up to the square root of `n`, and then lists fractions with 1 as the numerator and each divisor `d` of `n` as the denominator, where `n` is an integer strictly larger than 2 and the divisors are considered up to the square root of `n`.
#Overall this is what the function does:This function determines if a given integer `n` has any divisors other than 1 and itself, and if so, lists these divisors and their corresponding fractions. The function accepts an integer `n` between 2 and 10^9 and returns either 'NO' if `n` is less than or equal to 2 or has no divisors other than 1 and itself, or a string that confirms the presence of divisors, lists them, and includes their corresponding fractions. The function considers divisors up to the square root of `n`, ensuring that all divisors are found due to the mathematical property that a larger factor of the number would be a multiple of a smaller factor that has already been accounted for. If divisors are found, the function returns a string that starts with 'YES', followed by the count of divisors (including their corresponding quotients if they are not equal to the divisor), and then lists fractions with 1 as the numerator and each divisor as the denominator. The function handles edge cases where `n` is less than or equal to 2, and where `n` is a prime number (i.e., has no divisors other than 1 and itself), returning 'NO' in these cases.

