#State of the program right berfore the function call: Input consists of several datasets with each dataset containing an integer n, where 1 ≤ n ≤ 999,999. The total number of datasets is less than or equal to 30.
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 elements, where `a[i]` is True if `i` is a prime number, and False otherwise.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 elements; the count of `True` values in `a[1:int(s)]` is printed for each value of `s` read from `sys.stdin`.
#Overall this is what the function does:The function reads up to 30 integers from standard input, each representing a value `n` (1 ≤ n ≤ 999,999). It uses the Sieve of Eratosthenes to determine which numbers up to 1,000,000 are prime, storing the results in a list. For each integer `n` read, the function counts and prints the number of prime numbers less than or equal to `n`. The function does not return any value but outputs the count of primes for each input directly.

