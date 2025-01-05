#State of the program right berfore the function call: The input consists of multiple datasets, each containing an integer n where 1 ≤ n ≤ 999,999, and the total number of datasets does not exceed 30.
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 elements, where indices corresponding to prime numbers are set to True and all other indices are set to False.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 elements with prime indices set to True; the output is the count of True values in `a` from index 1 to `int(s)` for each input received from `sys.stdin`.
#Overall this is what the function does:The function accepts multiple datasets of integers, where each integer n is in the range of 1 to 999,999, and counts the number of prime numbers from 1 to n for each input. It uses the Sieve of Eratosthenes algorithm to determine which numbers are prime, storing the results in a list. The function then prints the count of prime numbers for each input dataset. Note that if the input is less than 1 or greater than 999,999, the behavior is not defined, as there are no error checks for invalid inputs.

