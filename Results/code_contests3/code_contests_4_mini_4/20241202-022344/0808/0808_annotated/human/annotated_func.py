#State of the program right berfore the function call: The function reads multiple datasets, each consisting of a single integer n, where 1 ≤ n ≤ 999,999. The total number of datasets is less than or equal to 30.
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 values where indices corresponding to non-prime numbers are set to `False` and indices corresponding to prime numbers are set to `True`, `i` is 1000000, and `j` is undefined.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 values with indices corresponding to non-prime numbers set to `False` and indices corresponding to prime numbers set to `True`; `i` is 1000000; `j` is undefined; the output consists of counts of prime numbers for each value read from `sys.stdin` or no output if no input was provided.
#Overall this is what the function does:The function initializes a list to determine the primality of numbers from 1 to 999,999. It then reads multiple datasets from standard input, each consisting of a single integer n (where 1 ≤ n ≤ 999,999), and prints the count of prime numbers up to each n. The function handles up to 30 datasets and does not return any value, only printing the results. If no input is provided, there will be no output.

