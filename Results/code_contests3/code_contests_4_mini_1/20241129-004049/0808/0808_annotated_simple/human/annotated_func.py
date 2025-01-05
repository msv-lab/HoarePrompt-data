#State of the program right berfore the function call: The function reads multiple integers n from input, where each n is a natural number satisfying 1 ≤ n ≤ 999,999, and the total number of datasets is less than or equal to 30.
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 values, where the indices corresponding to non-prime numbers are set to `False` and the indices corresponding to prime numbers remain `True`.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 values where indices corresponding to non-prime numbers are set to `False` and indices corresponding to prime numbers remain `True`; the count of `True` values in the slice `a[1:int(s)]` is printed for each input value from `sys.stdin`.
#Overall this is what the function does:The function reads multiple natural numbers from input (each between 1 and 999,999) and, for each input number, it counts and prints the number of prime numbers less than or equal to that input. It first generates a list indicating which numbers up to 999,999 are prime using the Sieve of Eratosthenes algorithm. The function does not handle cases where the input is not a valid natural number within the specified range or when there are more than 30 inputs.

