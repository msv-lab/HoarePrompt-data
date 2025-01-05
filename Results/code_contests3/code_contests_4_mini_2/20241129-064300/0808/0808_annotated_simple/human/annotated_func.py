#State of the program right berfore the function call: Each dataset consists of an integer n such that 1 ≤ n ≤ 999,999, and there are at most 30 datasets provided.
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 elements where `a[0]` and `a[1]` are False, `a[2]`, `a[3]`, `a[4]`, `a[5]`, `a[6]`, `a[7]`, etc. up to `a[999,999]` are True for prime indices and False for non-prime indices.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 elements where `a[0]` and `a[1]` are False, and `a[2]`, `a[3]`, `a[4]`, `a[5]`, `a[6]`, `a[7]`, etc. are True for prime indices and False for non-prime indices; the output is the count of `True` values in `a` for each input read from `sys.stdin`.
#Overall this is what the function does:The function initializes a list of Boolean values to identify prime numbers up to 999,999. It then reads multiple datasets (up to 30) from standard input, each containing an integer `n` (where 1 ≤ n ≤ 999,999), and prints the count of prime numbers less than or equal to `n`. The function does not accept parameters directly and handles input internally.

