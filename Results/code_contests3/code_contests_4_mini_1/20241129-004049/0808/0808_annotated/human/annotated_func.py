#State of the program right berfore the function call: The function reads multiple datasets, each containing an integer n where 1 ≤ n ≤ 999,999, and the total number of datasets is less than or equal to 30.
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `n` is an integer where 1 ≤ `n` ≤ 999,999, `a` is an array where `a[i]` is True if `i` is prime and False if `i` is composite for indices from 1 to 999,999.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `n` is an integer where 1 ≤ `n` ≤ 999,999; `s` is the last line of input from sys.stdin; the output for each input line is the count of prime numbers from 1 to `int(s)` based on the array `a`, where `a[i]` is True if `i` is prime and False if `i` is composite.
#Overall this is what the function does:The function reads multiple datasets of integers `n` (where 1 ≤ n ≤ 999,999) from standard input and counts the number of prime numbers from 1 to `n` for each input line. It uses the Sieve of Eratosthenes to identify prime numbers, storing the results in a boolean array `a`, where `a[i]` is True if `i` is prime. The function does not accept any parameters and directly prints the count of primes for each dataset provided until the end of input. It does not handle any edge cases explicitly, such as input errors or scenarios where `n` is outside the specified range.

