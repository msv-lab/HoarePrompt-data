#State of the program right berfore the function call: Each dataset consists of an integer n where 1 ≤ n ≤ 999,999 and the number of datasets is less than or equal to 30.
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 elements where indices that are not prime numbers are set to False and prime indices are set to True.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 elements where indices that are not prime numbers are set to False and prime indices are set to True; the count of True values from index 1 to `int(s)` is printed for each input value `s`.
#Overall this is what the function does:The function does not accept any parameters and calculates the count of prime numbers from 1 up to a given integer `n` (where 1 ≤ n ≤ 999,999) for multiple datasets. It prints the number of prime numbers for each provided value of `n`, accumulating results for up to 30 datasets. The function utilizes the Sieve of Eratosthenes algorithm for efficient prime number identification, with the list `a` indicating the primality of numbers up to 1,000,000.

