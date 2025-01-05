#State of the program right berfore the function call: The input consists of multiple datasets, each containing a single integer n where 1 ≤ n ≤ 999,999, and there are at most 30 datasets.
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 values where `a[i]` is `True` if `i` is a prime number and `False` otherwise, with `a[0]` and `a[1]` being `False`.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 values where `a[i]` is `True` if `i` is a prime number and `False` otherwise; `s` is the last line of input processed; the command prints the count of `True` values in `a[1:int(s)]` for each input line read.
#Overall this is what the function does:The function processes multiple datasets of integers, each representing a value `n` within the range of 1 to 999,999. It generates a list indicating whether each integer up to 1,000,000 is prime and then outputs the count of prime numbers for each input value `n`. However, the function does not return any value; it only prints the counts directly to the standard output for each dataset processed.

