#State of the program right berfore the function call: The function reads multiple datasets, each containing an integer n (1 ≤ n ≤ 999,999), with a maximum of 30 datasets in total.
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 elements where all indices that are not prime numbers are `False`, and indices that are prime numbers remain `True`.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `a` contains 1,000,000 elements with prime indices as `True`; the count of `True` values from index 1 to `int(s)` is printed for each input value of `s`.
#Overall this is what the function does:The function reads multiple datasets of integers `n` (1 ≤ n ≤ 999,999) from standard input, processes them to identify prime numbers up to 1,000,000, and prints the count of prime numbers for each dataset. It does not accept any parameters and does not handle cases where the input integer is less than 1 or greater than 999,999, which could lead to unexpected behavior.

