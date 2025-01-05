#State of the program right berfore the function call: The function reads multiple datasets consisting of integers n, where each n is a natural number such that 1 ≤ n ≤ 999,999, and there are at most 30 datasets.
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `a` is a list of length 1000000 with all elements set to True except for indices that are not prime, which are set to False.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `a` is a list of length 1000000 with all elements set to True except for indices that are not prime; the count of True values in `a` from index 1 to the maximum value received from `sys.stdin` is printed for each input value.
#Overall this is what the function does:The function reads multiple natural numbers (n) from standard input, where each n can range from 1 to 999,999, and counts the number of prime numbers less than or equal to each n. It uses the Sieve of Eratosthenes algorithm to precompute a list indicating prime status for numbers up to 999,999, and prints the count of prime numbers for each input value. The function does not return any value directly.

