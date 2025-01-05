#State of the program right berfore the function call: The input consists of several datasets, each containing an integer n where 1 ≤ n ≤ 999,999, and the number of datasets is less than or equal to 30.
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 elements where `a[i]` is `True` if `i` is a prime number and `False` otherwise, for `i` in the range from 2 to 999,999.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 elements where `a[i]` is `True` if `i` is a prime number; `s` is the last line of input read from stdin; the count of primes from 2 to `int(s)` is printed for each input line read.
#Overall this is what the function does:The function accepts multiple integers from standard input, each representing a value `n` (where 1 ≤ n ≤ 999,999), and for each value, it counts and prints the number of prime numbers less than or equal to `n` using a sieve algorithm. The function does not return any values; it directly prints the results to the standard output for each input line. The function assumes valid input within specified constraints and does not handle cases where the input is outside this range.

