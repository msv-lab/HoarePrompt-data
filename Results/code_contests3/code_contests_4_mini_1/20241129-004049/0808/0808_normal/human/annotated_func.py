#State of the program right berfore the function call: Each dataset consists of an integer n such that 1 ≤ n ≤ 999,999, and there are at most 30 datasets.
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 elements where indices representing prime numbers are True and indices representing non-prime numbers are False.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 elements with indices representing prime numbers as True and non-prime numbers as False; the loop prints the count of prime numbers for each input value processed from `sys.stdin` until no more inputs are provided.
#Overall this is what the function does:The function counts and prints the number of prime numbers for each integer `n` read from standard input, where `n` can range from 1 to 999,999, using the Sieve of Eratosthenes algorithm to determine the prime numbers. It does not return any values but prints the results directly.

